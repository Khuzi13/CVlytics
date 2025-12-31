from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import uuid, os
from .predict_ats_score import generate_full_ats_report


    # path('', views.homePage),   # blank space mean first page that show on site
    # path('about-us/',views.aboutus),
    # path('service/',views.service),

def homePage(request):
    return render(request,'index.html')

def cv_checker(request):
    return render(request,'cv_checker.html')


def result(request):
    return render(request,'result.html')

def contact_us(request):
    print(request)
    return render(request,'contact_us.html')







# def upload_file(request):
#     if request.method == 'POST' and request.FILES.get('resume'):
#         uploaded_file = request.FILES['resume']

#         if len(request.POST.get('job_description')) != 0:
#             job_description = request.POST.get('job_description')
#         else:
#             job_description = None



#         # 🔹 Generate unique ID
#         unique_id = uuid.uuid4().hex

#         # 🔹 Keep original extension
#         ext = os.path.splitext(uploaded_file.name)[1]

#         # 🔹 New unique filename
#         new_filename = f"resume_{unique_id}{ext}"

#         fs = FileSystemStorage()
#         filename = fs.save(new_filename, uploaded_file)
#         file_url = fs.url(filename)

#         return render(
#             request,
#             'result.html',
#             {
#                 'file_name': new_filename,
#                 'file_size': uploaded_file.size,
#                 'file_url': file_url,
#                 'file_id': unique_id,
#                 'job_desc' : job_description
#             }
#         )

#     return render(request, 'cv_checker.html')




def upload_file(request):
    if request.method == 'POST' and request.FILES.get('resume'):
        uploaded_file = request.FILES['resume']
        job_description = request.POST.get('job_description') or None

        unique_id = uuid.uuid4().hex
        ext = os.path.splitext(uploaded_file.name)[1]
        new_filename = f"resume_{unique_id}{ext}"

        fs = FileSystemStorage()
        filename = fs.save(new_filename, uploaded_file)
        file_path = fs.path(filename)

        report = generate_full_ats_report(file_path, job_description)


        
        # return
        breakdown = report["Breakdown"]
        return render(request, 'result.html', {
            'file_name': new_filename,
            'ats_score': report["ATS_Score"],
            'parse_rate': report["Parse_Rate"],
            'jd_match': report["JD_Match"],
            'overall_score': report["Overall_Score"],

            'formatting_score': breakdown.get("Formatting_Structure"),
            'formatting_score_color': breakdown.get("Formatting_Structure")*10,
            'soft_skills_score': breakdown.get("Soft_Skills_Tone"),
            'soft_skills_score_color': breakdown.get("Soft_Skills_Tone")*10,
            'hard_skills_score': breakdown.get("Hard_Skills_Match") if job_description else breakdown.get("Hard_Skills_Strength"),
            'ai_suggestion_1': report["AI_Suggestions"][0] ,
            'ai_suggestion_2': report["AI_Suggestions"][1] ,
            'ai_suggestion_3': report["AI_Suggestions"][2] ,
            'ai_suggestion_4': report["AI_Suggestions"][3] ,
        })

        # return render(request, 'result.html', {
        #     'file_name': new_filename,
        #     'ats_score': report["ATS_Score"],
        #     'parse_rate': report["Parse_Rate"],
        #     'jd_match': report["JD_Match"],
        #     'overall_score': report["Overall_Score"],
        #     'breakdown': report["Breakdown"],
        #     'ai_suggestions': report["AI_Suggestions"],
        # })

    return render(request, 'cv_checker.html')


def upload_file(request):
    if request.method == 'POST' and request.FILES.get('resume'):
        uploaded_file = request.FILES['resume']
        job_description = request.POST.get('job_description') or None

        unique_id = uuid.uuid4().hex
        ext = os.path.splitext(uploaded_file.name)[1]
        new_filename = f"resume_{unique_id}{ext}"

        fs = FileSystemStorage()
        filename = fs.save(new_filename, uploaded_file)
        file_path = fs.path(filename)

        report = generate_full_ats_report(file_path, job_description)

        # Always define breakdown FIRST
        breakdown = report.get("Breakdown", {})

        # Safe values
        formatting_value = breakdown.get("Formatting_Structure", 0)
        soft_skill_value = breakdown.get("Soft_Skills_Tone", 0)

        if job_description:
            hard_skill_value = breakdown.get("Hard_Skills_Match", 0)
        else:
            hard_skill_value = breakdown.get("Hard_Skills_Strength", 0)

        # Colors
        formatting_color = int(formatting_value * 10)
        soft_skill_color = int(soft_skill_value * 10)
        hard_skill_color = int(hard_skill_value * 10)

        # AI suggestions safety
        ai_list = report.get("AI_Suggestions", [])
        ai_list += [""] * (4 - len(ai_list))  # ensure 4 items

        return render(request, "result.html", {
            "file_name": new_filename,
            "ats_score": report["ATS_Score"],
            "parse_rate": report["Parse_Rate"],
            "jd_match": report["JD_Match"],
            "overall_score": report["Overall_Score"],

            "formatting_score": formatting_value,
            "formatting_score_color": formatting_color,

            "soft_skills_score": soft_skill_value,
            "soft_skills_score_color": soft_skill_color,

            "hard_skills_score": hard_skill_value,
            "hard_skills_score_color": hard_skill_color,

            "ai_suggestion_1": ai_list[0],
            "ai_suggestion_2": ai_list[1],
            "ai_suggestion_3": ai_list[2],
            "ai_suggestion_4": ai_list[3],
        })
