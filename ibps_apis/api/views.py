from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
import pandas as pd
import os

User = get_user_model()

# ==============================
# 1. Simple UI Login (for demo)
# ==============================
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate using Django User
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session["user"] = username

            # Generate JWT tokens properly
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return redirect(f"/jobs/?token={access_token}")

        return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")


# ===========================================
# 2. Jobs Page — Loads Scraped CSV into HTML
# ===========================================
def jobs_page(request):
    # Construct path relative to project root
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    csv_path = os.path.join(base_dir, "ibps_jobs.csv")

    jobs = []
    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path)
            jobs = df.to_dict(orient="records")
        except Exception as e:
            print("Error reading CSV:", e)

    return render(request, "jobs.html", {"jobs": jobs})


# ==================================
# 3. JWT-Protected Example Endpoint
# ==================================
@api_view(['GET'])  # GET is typical for fetching data
@permission_classes([IsAuthenticated])
def protected_api(request):
    return Response({
        "message": f"Hello, {request.user.username}! You are authenticated via JWT."
    })
