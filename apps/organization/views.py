from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg, CityDict

# Create your views here.


class OrgList(View):
    """
    课程机构列表
    """
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by('-clickNum')[:3]
        all_cities = CityDict.objects.all()

        # 城市过滤
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 类别过滤
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)
        # 分页实现

        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs.order_by('-course_num')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 每夜显示的item的个数
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        org_nums = all_orgs.count()

        return render(request, 'org-list.html', {'all_orgs': orgs,
                                                 'all_cities': all_cities,
                                                 'org_nums': org_nums,
                                                 'city_id': city_id,
                                                 'category': category,
                                                 'hot_orgs': hot_orgs,
                                                 })