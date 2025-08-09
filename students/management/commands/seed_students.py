from django.core.management.base import BaseCommand
from students.models import Student

SAMPLE = [
    {
        "name": "Ava Tesfaye",
        "program": "M.S. Electrical & Computer Engineering",
        "university": "Duke University",
        "bio": "Researching neuromorphic devices, perovskite memristors, and energy-efficient computing.",
        "photo_url": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?q=80&w=800&auto=format&fit=crop",
        "profile_url": "https://www.linkedin.com/",
    },
    {
        "name": "Daniel Kim",
        "program": "Ph.D. Materials Science",
        "university": "Carnegie Mellon University",
        "bio": "Tight-binding models for wide bandgap oxides; DFT + Wannierization workflows.",
        "photo_url": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=800&auto=format&fit=crop",
        "profile_url": "https://www.linkedin.com/",
    },
    {
        "name": "Sara Johnson",
        "program": "B.S. Computer Engineering",
        "university": "Stanford University",
        "bio": "EDA + RL for congestion-aware global routing; Python/C++ tooling enthusiast.",
        "photo_url": "https://images.unsplash.com/photo-1547425260-76bcadfb4f2c?q=80&w=800&auto=format&fit=crop",
        "profile_url": "https://www.linkedin.com/",
    },
    {
        "name": "Yonatan Berhane",
        "program": "M.S. Mechanical Engineering",
        "university": "Old Dominion University",
        "bio": "Microfluidics and thermal transport; hardware-in-the-loop testing.",
        "photo_url": "https://images.unsplash.com/photo-1511367461989-f85a21fda167?q=80&w=800&auto=format&fit=crop",
        "profile_url": "https://www.linkedin.com/",
    },
]

class Command(BaseCommand):
    help = "Seed the database with sample students"

    def handle(self, *args, **options):
        created = 0
        for data in SAMPLE:
            obj, was_created = Student.objects.get_or_create(name=data["name"], defaults=data)
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Seeded {created} students (idempotent)."))
