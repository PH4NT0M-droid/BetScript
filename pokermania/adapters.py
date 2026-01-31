from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        """
        Populate required fields for custom User model
        """
        user = sociallogin.user

        email = data.get("email", "")
        name = data.get("name", "")

        # fallback username if required
        if not getattr(user, "username", None):
            user.username = email.split("@")[0]

        user.email = email

        return user