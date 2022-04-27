from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user( self, username, team_leader, email, password, **other_fields):
        """
        Create and save a User with the given email and password.

        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(username= username, team_leader= team_leader, email= email, **other_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, username, team_leader, email, password, **other_fields):
        """
        Create and save a SuperUser with the given email and password.
        """


        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, team_leader, email, password, **other_fields)