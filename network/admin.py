from django.contrib import admin


from .models import Search, City, Location, ContactType, Contact, User, Problem, Service, PropertyType, Property, Customer, Provider, CustomerData, ProviderData, RequestState, Request, Abstraction, VisibilityRule, Skill, ScoreSystem, ScoreSystemValue, ScoreProvider, ScoreCustomer
# Register your models here.


class SearchAdmin(admin.ModelAdmin):
    pass
admin.site.register(Search,SearchAdmin)

class CityAdmin(admin.ModelAdmin):
    pass
admin.site.register(City,CityAdmin)

class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Location,LocationAdmin)

class ContactTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContactType,ContactTypeAdmin)

class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact,ContactAdmin)

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User,UserAdmin)

class ProblemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Problem,ProblemAdmin)

class ServiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Service,ServiceAdmin)

class PropertyTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(PropertyType,PropertyTypeAdmin)

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer,CustomerAdmin)

class ProviderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Provider,ProviderAdmin)

class ProviderDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProviderData,ProviderDataAdmin)

class CustomerDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(CustomerData,CustomerDataAdmin)

class RequestStateAdmin(admin.ModelAdmin):
    pass
admin.site.register(RequestState,RequestStateAdmin)

class RequestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Request,RequestAdmin)

class AbstractionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Abstraction,AbstractionAdmin)
class VisibilityRuleAdmin(admin.ModelAdmin):
    pass
admin.site.register(VisibilityRule,VisibilityRuleAdmin)
class SkillAdmin(admin.ModelAdmin):
    pass
admin.site.register(Skill,SkillAdmin)
class ScoreSystemAdmin(admin.ModelAdmin):
    pass
admin.site.register(ScoreSystem,ScoreSystemAdmin)
class ScoreSystemValueAdmin(admin.ModelAdmin):
    pass
admin.site.register(ScoreSystemValue,ScoreSystemValueAdmin)
class ScoreProviderAdmin(admin.ModelAdmin):
    pass
admin.site.register(ScoreProvider,ScoreProviderAdmin)
class ScoreCustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(ScoreCustomer,ScoreCustomerAdmin)