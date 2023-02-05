from datetime import datetime
from django import template
import calendar
import dateutil.relativedelta

register = template.Library()


@register.inclusion_tag("months_list_tpl.html")
def get_last_months():
    months_list = []
    now = datetime.now()
    for month_count in range(12):
        date = now + dateutil.relativedelta.relativedelta(months=-month_count)
        month = calendar.month_name[date.month]
        year = date.year
        slug = f"{year}-{str(date.month).zfill(2)}"
        months_list.append([month, year, slug])
    return {"months_list": months_list}
