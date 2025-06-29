from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Requirement, Recommendation

def login_view(request):
    """Handle user login."""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('redirect_after_login') 
        messages.error(request, "Invalid credentials.")
    return render(request, 'registration/login.html')

def home_view(request):
    """Render the home page."""
    return render(request, 'assessment/home.html')

@login_required
def dashboard_view(request):
    """Render the dashboard page for logged-in users."""
    return render(request, 'assessment/dashboard.html')

@login_required
def information_view(request):
    """Render the information page for logged-in users."""
    return render(request, 'assessment/information.html')

@login_required
def assessment_view(request):
    """
    Handle Annex I assessment submission and render the form.
    """
    if request.method == "POST":
        annex1_data = {}
        for req in Requirement.objects.filter(requirement_class='annex_1'):
            answer_key = f'requirement_{req.id}'
            explanation_key = f'explanation_{req.id}'
            annex1_data[answer_key] = request.POST.get(answer_key)
            annex1_data[explanation_key] = request.POST.get(explanation_key, "")
        
        request.session['annex1_data'] = annex1_data
        return redirect('assessment_annex2')
    annex_1_reqs = Requirement.objects.filter(requirement_class='annex_1')
    return render(request, "assessment/form_annex1.html", {
        "annex_1_reqs": annex_1_reqs
    })

@login_required
def annex2_view(request):
    """
    Handle Annex II assessment submission and render the form.
    """
    if request.method == "POST":
        annex2_data = {}
        for req in Requirement.objects.filter(requirement_class='annex_2'):
            answer_key = f'requirement_{req.id}'
            explanation_key = f'explanation_{req.id}'
            annex2_data[answer_key] = request.POST.get(answer_key)
            annex2_data[explanation_key] = request.POST.get(explanation_key, "")
        
        request.session['annex2_data'] = annex2_data
        return redirect('assessment_vuln')
    annex_2_reqs = Requirement.objects.filter(requirement_class='annex_2')
    return render(request, "assessment/form_annex2.html", {
        "annex_2_reqs": annex_2_reqs
    })

def process_answers(answer_data):
    """Process stored data containing both answers and explanations"""
    answers = {k: v for k, v in answer_data.items() if k.startswith('requirement_')}
    explanations = {k.split('_')[1]: v for k, v in answer_data.items() 
                   if k.startswith('explanation_') and v}
    
    total = len(answers)
    compliant = 0
    recommendations = []
    
    for key, value in answers.items():
        req_id = key.split('_')[1]
        if value == "True":
            compliant += 1
        elif value == "Partial":
            compliant += 0.5
            recommendations.append(int(req_id))
        elif value == "False":
            recommendations.append(int(req_id))
    
    return total, compliant, recommendations, explanations

@login_required
def vulnerability_assessment_view(request):
    """
    Handle vulnerability assessment submission and render results or form.
    Now captures explanations for ALL sections (Annex I, II, and Vulnerability)
    """
    if request.method == "POST":
        # Process Annex I with explanations
        annex1_data = request.session.get('annex1_data', {})
        annex1_answers = {k: v for k, v in annex1_data.items() if k.startswith('requirement_')}
        annex1_explanations = {int(k.split('_')[1]): v for k, v in annex1_data.items() 
                              if k.startswith('explanation_') and v}
        annex1_total, annex1_compliant, annex1_recs = process_compliance(annex1_answers)
        
        # Process Annex II with explanations
        annex2_data = request.session.get('annex2_data', {})
        annex2_answers = {k: v for k, v in annex2_data.items() if k.startswith('requirement_')}
        annex2_explanations = {int(k.split('_')[1]): v for k, v in annex2_data.items() 
                              if k.startswith('explanation_') and v}
        annex2_total, annex2_compliant, annex2_recs = process_compliance(annex2_answers)
        
        # Process Vulnerability with explanations
        vuln_answers = {k: v for k, v in request.POST.items() if k.startswith('requirement_')}
        vuln_explanations = {int(k.split('_')[1]): v for k, v in request.POST.items() 
                            if k.startswith('explanation_') and v}
        vuln_total, vuln_compliant, vuln_recs = process_compliance(vuln_answers)
        
        # Combine and filter recommendations and explanations
        all_rec_ids = set(annex1_recs + annex2_recs + vuln_recs)
        recommendations = Recommendation.objects.filter(requirement_id__in=all_rec_ids)
        explanations = {**annex1_explanations, **annex2_explanations, **vuln_explanations}

        # Clear session data
        for key in ['annex1_data', 'annex2_data']:
            if key in request.session:
                del request.session[key]

        return render(request, "assessment/results.html", {
            "recommendations": recommendations,
            "explanations": explanations,
            "annex1_total": annex1_total,
            "annex1_implemented": annex1_compliant,
            "annex2_total": annex2_total,
            "annex2_implemented": annex2_compliant,
            "vuln_total": vuln_total,
            "vuln_implemented": vuln_compliant,
        })

    # GET: Load vulnerability questions
    vuln_reqs = Requirement.objects.filter(requirement_class='vuln')
    return render(request, "assessment/vuln_form.html", {
        "vuln_reqs": vuln_reqs,
    })


def process_compliance(answer_dict):
    """Calculate compliance scores and recommendations (without explanations)"""
    total = len(answer_dict)
    compliant = 0
    recommendations = []
    
    for key, value in answer_dict.items():
        req_id = int(key.split('_')[1])
        if value == "True":
            compliant += 1
        elif value == "Partial":
            compliant += 0.5
            recommendations.append(req_id)
        elif value == "False":
            recommendations.append(req_id)
    
    return total, compliant, recommendations

@login_required
def redirect_after_login_view(request):
    """Redirect user after login based on their role."""
    if request.user.is_superuser:
        return redirect('/admin/')
    return redirect('dashboard')
