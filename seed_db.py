import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumina_core.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Post

from accounts.models import Profile

# Delete existing admin user to ensure clean state
try:
    User.objects.get(username='admin').delete()
    print("Deleted existing admin user.")
except User.DoesNotExist:
    pass

# Create fresh superuser
user = User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
print(f"Admin user created. Username: admin, Password: adminpass")

# Create profile
Profile.objects.get_or_create(user=user)
print("Admin profile configured.")

# Clear existing posts to avoid duplicates/conflicts during dev
Post.objects.all().delete()

posts_data = [
    {
        "title": "Minimalism in Code",
        "subtitle": "How reducing complexity in your codebase leads to scalable and maintainable applications.",
        "category": "Tech",
        "color": "primary",
        "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuD3g_P74ear1WydbDSGURFRpW06CE-Iid_oXHRIDzFT-8FGsKEjj1Z2Xeu5i_9v-DI2okTyDUhcjzZcbT3l-CE_uWD1lGf29-RRgq0q4O1dH1IhMwtovMZ8dFqHo2L31yeFjNs8_IqNfYCtIKZBrSYgPi0eQDLRaWxzG1qFtai7zz7ceIYnR7A4poOaK-2a2IdM6xnQzPsbdZNc39QfuwnTUfIhO0NYcCDa64bSwvVQlnLFEN2OACG5uFcHrgldiDe2nsN_3wucLEY",
        "read_time": 5
    },
    {
        "title": "The Urban Photographer",
        "subtitle": "Capturing the soul of the city through the lens of street photography.",
        "category": "Art",
        "color": "purple-400",
        "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuCKXdczdPL1BHMhgohGpad218z6J46QIuvLkhj_2pPNy0tb9DsBLZ9XZpSZk6S5UAXWF7ikGAP2fzOakvVCFrGlZDP67fjSBdHmJCN5PFfB-UaNKksz836JD4WPaglreu2e7O56DloOvObWFAvWa_M-z4lBKszE1ZwNjCpknmUK_p2RfLO927dFKrDd99ICfB0g7mDZLHMNaWfyu6PEmRB_E4SDXd5nxNU6P0gSrPFFbgHNXcqxwNvcr3wmvZ7UAXlaUWMYWnl-bYI",
        "read_time": 3
    },
    {
        "title": "Remote Work Culture",
        "subtitle": "Building connection and company culture in a distributed world.",
        "category": "Lifestyle",
        "color": "green-400",
        "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuDo0NUVcnzz-ZzcVwMy_5Beqt8k1llySYpyXEcF_1jbYPwzaAbT5NT8qJV-DIU-MvaSf9s-Ka7YoIib_wm8dAk9ZuS2B_lbTOU6FE5EtV4pqpddsKQnsR8J7AxfLVNYTEQtv1lYGhAKlrxseEHtfcrzheSfUBz5Qlo1CodnOpHYTTtl-P0oYhXi0iKuR6-f5s9yR7SbylzwUOyr7xw11iDcmWMsSTAO1bsb_QOcEu4FU1t4p4Ut_73RVZy1mDJCX1IuPL_I6i6qv0k",
        "read_time": 6
    },
    {
        "title": "AI in Design",
        "subtitle": "Will artificial intelligence replace designers or empower them?",
        "category": "Design",
        "color": "pink-400",
        "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuB3MqzvLoIFB_I2y76snGYTy6-dRZgp_3z66Xk0SMV7iZqFJIvaj_oz_3KdsMU7ulK48FHON8VmSVluAJB-wlGdbegc4O4bx1nCV26SmS6qhhKPB3KJrV1YVjwfm370skwF1inbdJ9l3RbXynVg7GtMbspXuX4pLdmKkpJVMGMNnG0dl0lug6qMj-PonSUW4v_KzeDd42Yby52dNRbo2WXeColkNJHTD0vWRtYJ85PI1WecNePRWjXx9qKwXXD9mZ0S6nZ35OrfSmE",
        "read_time": 4
    },
    {
        "title": "Sustainable Living",
        "subtitle": "Small changes in your daily routine that make a big impact on the planet.",
        "category": "Life",
        "color": "yellow-400",
        "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuBqFO_d3nOw89pW5vFAKBE_eHLm3nGZVuYtY1ErTtvpRoXx-vA1wFlGszjDuKZbKhSTG1z4uEW-pvp4dsaGWYnnFcQIEtMvAfM8wsLW5I8NYzvL-RWPCpT-leyNKWarptisJEbzXFYc0UqR5dc6hOkkTtSuNdlDVsAYKdrHphb0ZY6OMWdIry_KwbazBOgOo_jFNHH1tD_7g6xzFyWrKte8FV-Ht55X42UUbhWoOT5tjOF7oFdyX9FAz1E5igvnarZ75i110vrerBA",
        "read_time": 5
    },
    {
        "title": "Modern Spaces",
        "subtitle": "Why brutalism is making a comeback in modern residential architecture.",
        "category": "Architecture",
        "color": "blue-400",
        "image_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuAVzyi4zpk74T26Bt9hnruJSI_Z2TAzfL_UPcu3L4PhQVa4-toDw_HM5nXCE6IRSmV7uCP0iUUItejP698slnskrYq-gxe5Mp-eGZkTjBy-sCXrZuQPMY7fcGehXvbUHKI11MuQWtrp12w9NM5M_Z0f1eyzyfBwZ1TTzM7TkC367H-wgtqbFC3mdj8ubtuiqC-UXwmL5ANNsw4vl1OYvLJLT5erlnvuOHA6g3kADFco3AiS5ZJwQ1VAEoOoxA6uC8s4Toa7ZbT25NM",
        "read_time": 7
    }
]

for post_data in posts_data:
    Post.objects.update_or_create(
        title=post_data['title'],
        defaults={
            'subtitle': post_data['subtitle'],
            'category': post_data['category'],
            'color': post_data['color'],
            # 'image_url': post_data['image_url'], # Removed as field changed to ImageField
            'read_time': post_data['read_time'],
            'content': f"""
<h2>Introduction</h2>
<p>This is a sample blog post about {post_data['title']}. It explores various aspects of the topic in depth.</p>

<h2>Key Concepts</h2>
<p>Here we discuss the main ideas behind {post_data['category']}. Understanding these principles is crucial.</p>

<h2>Future Outlook</h2>
<p>What does the future hold for {post_data['title']}? We examine potential trends and developments.</p>

<h3>Conclusion</h3>
<p>In summary, {post_data['title']} remains a significant subject in the world of {post_data['category']}.</p>
""",
            'author': user
        }
    )

print("Database seeded with new color schema!")
