import datetime

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FutureDateRangeValidator:
    def __init__(self,
                 min_interval_from_now=datetime.timedelta(days=1),
                 max_interval_from_now=datetime.timedelta(days=5)):
        self.min_interval_from_now = min_interval_from_now
        self.max_interval_from_now = max_interval_from_now

    def __call__(self, value):
        now = datetime.datetime.now(datetime.timezone.utc)
        if not now + self.min_interval_from_now < value < now + self.max_interval_from_now:
            raise ValidationError('Date must be today or later')
