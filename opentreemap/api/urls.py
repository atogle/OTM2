# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from django.conf.urls import patterns, url

from opentreemap.util import route

from api.views import (status_view, version_view,
                       remove_current_tree_from_plot, plots_endpoint,
                       species_list_endpoint, approve_pending_edit,
                       update_user_endpoint, reset_password, user_endpoint,
                       plot_endpoint, edits, plots_closest_to_point_endpoint,
                       instance_info_endpoint, add_photo_endpoint,
                       export_users_csv_endpoint, export_users_json_endpoint,
                       update_profile_photo_endpoint)

from treemap.instance import URL_NAME_PATTERN


instance_pattern = r'^(?P<instance_url_name>' + URL_NAME_PATTERN + r')'

urlpatterns = patterns(
    '',
    (r'^$', status_view),
    (r'^version$', version_view),

    (r'^user$', user_endpoint),
    url(r'^user/(?P<user_id>\d+)$', update_user_endpoint,
        name='update_user'),
    url(r'^user/(?P<user_id>\d+)/photo$', update_profile_photo_endpoint,
        name='update_user_photo'),
    (r'^user/(?P<user_id>\d+)/reset_password$', reset_password),
    (r'^user/(?P<user_id>\d+)/edits$', edits),

    (instance_pattern + r'/plots/(?P<plot_id>\d+)/tree/photo$',
     add_photo_endpoint),

    (instance_pattern + r'/plots/(?P<plot_id>\d+)/tree$',
     route(DELETE=remove_current_tree_from_plot)),

    (instance_pattern + r'/pending-edits/(?P<pending_edit_id>\d+)/approve',
     route(POST=approve_pending_edit)),

    (instance_pattern + r'/pending-edits/(?P<pending_edit_id>\d+)/reject',
     route(POST=reject_pending_edit)),

    # OTM2/instance endpoints
    (instance_pattern + '$', instance_info_endpoint),
    (instance_pattern + '/species$', species_list_endpoint),
    (instance_pattern + r'/plots$', plots_endpoint),
    (instance_pattern + r'/plots/(?P<plot_id>\d+)$',
     plot_endpoint),
    (instance_pattern + r'/locations/'
     '(?P<lat>-{0,1}\d+(\.\d+){0,1}),(?P<lng>-{0,1}\d+(\.\d+){0,1})'
     '/plots', plots_closest_to_point_endpoint),

    url(instance_pattern + r'/users.csv',
        export_users_csv_endpoint, name='user_csv'),
    url(instance_pattern + r'/users.json',
        export_users_json_endpoint, name='user_json'),
)
