from decimal import Decimal

from django.core.management.base import BaseCommand

from products.models import Category, Product


PLACEHOLDER_IMAGE = "products/fashion-placeholder.svg"


def unsplash_url(photo_id):
    return f"https://unsplash.com/photos/{photo_id}/download?force=true&w=1200"


PRODUCTS = [
    {
        "name": "Men's Cotton T-Shirt",
        "price": Decimal("799.00"),
        "description": "Soft combed cotton t-shirt with a regular fit and breathable finish for everyday wear.",
        "brand": "Urban Thread",
        "stock": 48,
        "category": "Men",
        "image_url": unsplash_url("CKiRgZO0vQo"),
    },
    {
        "name": "Slim Fit Denim Jeans",
        "price": Decimal("1799.00"),
        "description": "Stretch denim jeans with a slim silhouette, mid-rise waist, and all-day comfort.",
        "brand": "Blue Ridge",
        "stock": 30,
        "category": "Men",
        "image_url": unsplash_url("btqQFG47URw"),
    },
    {
        "name": "Casual Hoodie",
        "price": Decimal("1599.00"),
        "description": "Fleece-lined hoodie with a clean front, drawstring hood, and relaxed streetwear styling.",
        "brand": "North Lane",
        "stock": 24,
        "category": "Men",
        "image_url": unsplash_url("rtZNrTpbi5g"),
    },
    {
        "name": "Leather Jacket",
        "price": Decimal("4599.00"),
        "description": "Classic faux leather jacket with zip closure, structured collar, and a sleek modern cut.",
        "brand": "Rogue Studio",
        "stock": 12,
        "category": "Men",
        "image_url": unsplash_url("fIkxrvBI2eU"),
    },
    {
        "name": "Denim Jacket",
        "price": Decimal("2399.00"),
        "description": "Mid-wash denim jacket with contrast stitching and an easy layered fit for daily wear.",
        "brand": "Street Foundry",
        "stock": 21,
        "category": "Men",
        "image_url": unsplash_url("cThejPg4qUQ"),
    },
    {
        "name": "Checked Flannel Shirt",
        "price": Decimal("1399.00"),
        "description": "Brushed cotton flannel shirt with button front, chest pockets, and a soft hand feel.",
        "brand": "Timber & Co.",
        "stock": 27,
        "category": "Men",
        "image_url": unsplash_url("w1i5pJGc6dY"),
    },
    {
        "name": "Men's Bomber Jacket",
        "price": Decimal("3299.00"),
        "description": "Lightweight bomber jacket with ribbed cuffs and a clean urban silhouette.",
        "brand": "Aero Form",
        "stock": 15,
        "category": "Men",
        "image_url": unsplash_url("ug3tOIPtTO8"),
    },
    {
        "name": "Women's Summer Floral Dress",
        "price": Decimal("2299.00"),
        "description": "Lightweight floral dress with a flowy hemline and flattering waist detail for warm days.",
        "brand": "Bloom & Co.",
        "stock": 22,
        "category": "Women",
        "image_url": unsplash_url("KcERAQcCGmw"),
    },
    {
        "name": "High-Rise Pleated Skirt",
        "price": Decimal("1499.00"),
        "description": "Elegant pleated midi skirt with a comfortable waistband and versatile day-to-evening styling.",
        "brand": "Grace Avenue",
        "stock": 18,
        "category": "Women",
        "image_url": unsplash_url("rmdwE76Uif4"),
    },
    {
        "name": "Women's Linen Co-ord Set",
        "price": Decimal("2899.00"),
        "description": "Two-piece linen blend set with a tailored shirt and matching trousers for effortless dressing.",
        "brand": "Mira Mode",
        "stock": 16,
        "category": "Women",
        "image_url": unsplash_url("zkFGRW9CKww"),
    },
    {
        "name": "Ribbed Knit Cardigan",
        "price": Decimal("1899.00"),
        "description": "Soft ribbed cardigan with tonal buttons and a cozy fit for layering through the season.",
        "brand": "Willow Wear",
        "stock": 20,
        "category": "Women",
        "image_url": unsplash_url("0hbEGg_LeUY"),
    },
    {
        "name": "Women's Satin Blouse",
        "price": Decimal("1699.00"),
        "description": "Fluid satin blouse with a clean drape, soft sheen, and desk-to-dinner versatility.",
        "brand": "Luna Atelier",
        "stock": 19,
        "category": "Women",
        "image_url": unsplash_url("BQ9b7sE9Kvk"),
    },
    {
        "name": "Women's Wide-Leg Trousers",
        "price": Decimal("1899.00"),
        "description": "Tailored wide-leg trousers with a high-rise fit and easy movement for polished styling.",
        "brand": "Mira Mode",
        "stock": 23,
        "category": "Women",
        "image_url": unsplash_url("s-4maxr-W78"),
    },
    {
        "name": "Women's Floral Maxi Dress",
        "price": Decimal("2699.00"),
        "description": "Printed maxi dress with airy fabric, soft gathers, and a graceful silhouette.",
        "brand": "Bloom & Co.",
        "stock": 14,
        "category": "Women",
        "image_url": unsplash_url("mbAhuEaVXqg"),
    },
    {
        "name": "Women's Cropped Cardigan",
        "price": Decimal("1499.00"),
        "description": "Button-front cropped cardigan with a compact knit and clean shape for layering.",
        "brand": "Softline",
        "stock": 17,
        "category": "Women",
        "image_url": unsplash_url("Q5L794dp-Zg"),
    },
    {
        "name": "Women's Printed Kimono",
        "price": Decimal("1599.00"),
        "description": "Open-front printed kimono designed for effortless layering over basics and dresses.",
        "brand": "Rose Theory",
        "stock": 13,
        "category": "Women",
        "image_url": unsplash_url("hj_ArSQQ0FI"),
    },
    {
        "name": "Girls Floral Party Dress",
        "price": Decimal("1499.00"),
        "description": "Soft party dress with floral accents, flutter sleeves, and a comfortable inner lining.",
        "brand": "Little Bloom",
        "stock": 26,
        "category": "Kids",
        "image_url": unsplash_url("COgVvJ_CG_I"),
    },
    {
        "name": "Kids Graphic Sweatshirt",
        "price": Decimal("1199.00"),
        "description": "Playful cotton sweatshirt with soft brushed lining and easy everyday comfort for kids.",
        "brand": "Little Orbit",
        "stock": 26,
        "category": "Kids",
        "image_url": unsplash_url("5oM8cOCQ8cQ"),
    },
    {
        "name": "Boys Cargo Joggers",
        "price": Decimal("999.00"),
        "description": "Flexible joggers with utility pockets, elastic waist, and a comfortable tapered fit.",
        "brand": "Tiny Trek",
        "stock": 32,
        "category": "Kids",
        "image_url": unsplash_url("5oM8cOCQ8cQ"),
    },
    {
        "name": "Kids Puffer Vest",
        "price": Decimal("1399.00"),
        "description": "Lightweight padded vest with zip closure and easy layering for outdoor play.",
        "brand": "Trail Cubs",
        "stock": 18,
        "category": "Kids",
        "image_url": unsplash_url("5oM8cOCQ8cQ"),
    },
    {
        "name": "Girls Everyday Leggings",
        "price": Decimal("699.00"),
        "description": "Stretch jersey leggings with a soft waistband and flexible fit for all-day movement.",
        "brand": "Little Bloom",
        "stock": 34,
        "category": "Kids",
        "image_url": unsplash_url("COgVvJ_CG_I"),
    },
    {
        "name": "Kids Printed T-Shirt",
        "price": Decimal("649.00"),
        "description": "Everyday printed tee in breathable cotton with a playful, easy-to-style finish.",
        "brand": "Mini Street",
        "stock": 40,
        "category": "Kids",
        "image_url": unsplash_url("COgVvJ_CG_I"),
    },
    {
        "name": "Running Sneakers",
        "price": Decimal("2599.00"),
        "description": "Lightweight running sneakers with cushioned soles, mesh panels, and reliable traction.",
        "brand": "StrideX",
        "stock": 35,
        "category": "Shoes",
        "image_url": unsplash_url("aFb6gwo9aT8"),
    },
    {
        "name": "Minimal White Trainers",
        "price": Decimal("2199.00"),
        "description": "Clean low-top trainers designed for casual wear with padded support and easy pairing.",
        "brand": "City Step",
        "stock": 28,
        "category": "Shoes",
        "image_url": unsplash_url("HyfBIObAA4Y"),
    },
    {
        "name": "Retro Basketball Shoes",
        "price": Decimal("2899.00"),
        "description": "Court-inspired high-top sneakers with contrast panels and cushioned ankle support.",
        "brand": "Jump Route",
        "stock": 18,
        "category": "Shoes",
        "image_url": unsplash_url("rNaD91H95WY"),
    },
    {
        "name": "Performance Training Shoes",
        "price": Decimal("2499.00"),
        "description": "Breathable training shoes with grippy soles and lightweight support for daily workouts.",
        "brand": "Motion Lab",
        "stock": 22,
        "category": "Shoes",
        "image_url": unsplash_url("CEDkze7NIH0"),
    },
    {
        "name": "Colorblock Sport Sneakers",
        "price": Decimal("2399.00"),
        "description": "Bold sneakers with colorblock details, cushioned midsoles, and street-ready styling.",
        "brand": "StrideX",
        "stock": 20,
        "category": "Shoes",
        "image_url": unsplash_url("Ngxjs5fVBNc"),
    },
    {
        "name": "Canvas Slip-On Shoes",
        "price": Decimal("1499.00"),
        "description": "Easy-wear slip-ons with a lightweight canvas upper and flexible rubber sole.",
        "brand": "Harbor Mile",
        "stock": 29,
        "category": "Shoes",
        "image_url": unsplash_url("HyfBIObAA4Y"),
    },
    {
        "name": "Classic Leather Belt",
        "price": Decimal("999.00"),
        "description": "Polished leather-look belt with a durable metal buckle and refined everyday styling.",
        "brand": "Craftline",
        "stock": 40,
        "category": "Accessories",
        "image_url": unsplash_url("qbAl_t6ps2M"),
    },
    {
        "name": "Structured Tote Bag",
        "price": Decimal("2499.00"),
        "description": "Spacious tote with a clean silhouette, inner pocket layout, and premium textured finish.",
        "brand": "Aster Atelier",
        "stock": 14,
        "category": "Accessories",
        "image_url": unsplash_url("A3CTF4T_erU"),
    },
    {
        "name": "Canvas Shopper Bag",
        "price": Decimal("1299.00"),
        "description": "Durable everyday shopper with roomy capacity and a clean, versatile shape.",
        "brand": "Carry Theory",
        "stock": 25,
        "category": "Accessories",
        "image_url": unsplash_url("PENodSVsL1s"),
    },
    {
        "name": "Leather Crossbody Bag",
        "price": Decimal("2799.00"),
        "description": "Compact crossbody with an adjustable strap, organized interior, and polished finish.",
        "brand": "Aster Atelier",
        "stock": 11,
        "category": "Accessories",
        "image_url": unsplash_url("EQzfTYsFr2M"),
    },
    {
        "name": "Macrame Tote Bag",
        "price": Decimal("1599.00"),
        "description": "Textured handcrafted tote with fringe detail and a relaxed artisanal look.",
        "brand": "Solea Studio",
        "stock": 16,
        "category": "Accessories",
        "image_url": unsplash_url("ddNtzPcgfr8"),
    },
    {
        "name": "Round Dial Watch",
        "price": Decimal("1999.00"),
        "description": "Classic analog watch with a leather-look strap and clean minimal dial.",
        "brand": "Hourmark",
        "stock": 19,
        "category": "Accessories",
        "image_url": unsplash_url("qbAl_t6ps2M"),
    },
    {
        "name": "Colorblock Tote Collection",
        "price": Decimal("1899.00"),
        "description": "Fashion-forward tote design with color-rich panels and a practical carry shape.",
        "brand": "Carry Theory",
        "stock": 17,
        "category": "Accessories",
        "image_url": unsplash_url("XXLfSKryuYE"),
    },
]


class Command(BaseCommand):
    help = "Seed the database with a realistic ecommerce fashion catalog."

    def handle(self, *args, **options):
        categories = {}
        for category_name in ["Women", "Men", "Kids", "Shoes", "Accessories"]:
            category, _ = Category.objects.get_or_create(name=category_name)
            categories[category_name] = category

        created_count = 0
        updated_count = 0

        for item in PRODUCTS:
            product, created = Product.objects.update_or_create(
                name=item["name"],
                defaults={
                    "price": item["price"],
                    "description": item["description"],
                    "brand": item["brand"],
                    "stock": item["stock"],
                    "category": categories[item["category"]],
                    "image": PLACEHOLDER_IMAGE,
                    "image_url": item["image_url"],
                },
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seed complete: {created_count} created, {updated_count} updated."
            )
        )
