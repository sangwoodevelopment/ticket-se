from .models import FavoriteCompany, RecentView, VisitorCount
from django.utils import timezone


def side_company_box(request):
    if not request.user.is_authenticated:
        return {
            "side_favorites": [],
            "side_recent_companies": [],
        }

    favorites = (
        FavoriteCompany.objects
        .filter(user=request.user)
        .select_related("company")
        .order_by("-created_at")[:5]
    )

    recent = (
        RecentView.objects
        .filter(user=request.user)
        .select_related("company")
        .order_by("-viewed_at")[:5]
    )

    return {
        "side_favorites": favorites,
        "side_recent_companies": recent,
    }

def visitor_count(request):
    today = timezone.now().date()

    today_obj = VisitorCount.objects.filter(date=today).first()
    today_count = today_obj.count if today_obj else 0

    total_count = sum(VisitorCount.objects.values_list('count', flat=True))

    return{
        'today_visitor':today_count,
        'total_visitor':total_count,
    }