# Copyright 2012 Concentric Sky, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from django.conf import settings
from django.db import models
from django.utils import timezone


class InvitedUser(models.Model):
    STATUS_INVITED = 'invited'
    STATUS_REGISTERED = 'registered'
    STATUS_CHOICES = (
        (STATUS_INVITED, "Invited"),
        (STATUS_REGISTERED, "Registered"),
    )
    email = models.EmailField(max_length=254, unique=True)
    status = models.CharField(max_length=32, blank=True, choices=STATUS_CHOICES)
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    # We need to fake a few properties so we can use the default token generation code
    @property
    def last_login(self):
        if self.created_user and hasattr('last_login', self.created_user):
            return self.created_user.last_login
        else:
            return timezone.now()

    @property
    def password(self):
        return ''
