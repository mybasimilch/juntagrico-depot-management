from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from juntagrico.dao.subscriptiondao import SubscriptionDao

from juntagrico.views import get_menu_dict
from juntagrico.util.views_admin import subscription_management_list
from juntagrico.mailer import MemberNotification
from juntagrico.entity.subs import Subscription
from juntagrico.util import return_to_previous_location


@login_required
def depot_change_overview(request):
    renderdict = get_menu_dict(request)
    renderdict.update({
        'menu': {'dm': 'active'},
        'change_date_disabled': True,
    })
    changedlist = []
    changedlist = SubscriptionDao.subscritions_with_future_depots()
    return subscription_management_list(changedlist, renderdict, "dm/depot_change_overview.html", request)

@permission_required("juntagrico.is_operations_group")
def activate_future_depot(request,subscription_id):
    subscription = get_object_or_404(Subscription, id=subscription_id)
    subscription.depot = subscription.future_depot
    subscription.future_depot = None
    subscription.save()
    emails = []
    for member in subscription.recipients:
        emails.append(member.email)
    MemberNotification.depot_changed(emails, subscription.depot)
    return return_to_previous_location(request)
