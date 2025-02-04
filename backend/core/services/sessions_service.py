# from django.contrib.auth import user_logged_in
# from django.dispatch.dispatcher import receiver
# from django.contrib.sessions.models import Session
#
# from apps.user_sessions.models import UserSession
#
#
# @receiver(user_logged_in)    ## todo here is start of sessions creating
# def register_session(sender, user, request, **kwargs):
#
#     # save current session
#     request.session.save()
#
#     # create a link from the user to the current session (for later usage)
#     s = UserSession.objects.get_or_create(
#         user=user,
#         # session=Session.objects.get(pk=request.session.session_key)
#         session=Session.objects.get(pk=request.session.session_key)
#     )
#     print(s.keys().values)
#
#     # # може отак присвоїти закінчення і вийти
#     # if request.session['name'] == 'SRJ':
#     #     pass
