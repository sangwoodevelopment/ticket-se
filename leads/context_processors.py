from .models import FavoriteCompany, RecentView


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