"""
Wedding invitation templates for Amore.
Each template defines a canvas size and a list of elements.
Element types: text, shape, image_placeholder
"""

TEMPLATES: dict = {
    "classic_elegance": {
        "canvas": {"width": 1080, "height": 1350, "background": "#FFFFF5"},
        "elements": [
            {
                "id": "border_top",
                "type": "shape",
                "shape": "rect",
                "x": 40, "y": 40, "width": 1000, "height": 6,
                "fill": "#B8860B"
            },
            {
                "id": "border_bottom",
                "type": "shape",
                "shape": "rect",
                "x": 40, "y": 1304, "width": 1000, "height": 6,
                "fill": "#B8860B"
            },
            {
                "id": "title",
                "type": "text",
                "text": "Wedding Invitation",
                "x": 540, "y": 160,
                "fontSize": 52,
                "fontFamily": "Georgia, serif",
                "color": "#4A3728",
                "align": "center",
                "bold": False,
                "italic": True
            },
            {
                "id": "divider",
                "type": "text",
                "text": "— ✦ —",
                "x": 540, "y": 260,
                "fontSize": 28,
                "fontFamily": "Georgia, serif",
                "color": "#B8860B",
                "align": "center"
            },
            {
                "id": "names",
                "type": "text",
                "text": "Emma & James",
                "x": 540, "y": 380,
                "fontSize": 88,
                "fontFamily": "Georgia, serif",
                "color": "#2C1810",
                "align": "center",
                "bold": False
            },
            {
                "id": "together_label",
                "type": "text",
                "text": "Together with their families request the pleasure of your company",
                "x": 540, "y": 520,
                "fontSize": 26,
                "fontFamily": "Georgia, serif",
                "color": "#6B5744",
                "align": "center",
                "italic": True
            },
            {
                "id": "ceremony_label",
                "type": "text",
                "text": "AT THE CELEBRATION OF THEIR MARRIAGE",
                "x": 540, "y": 640,
                "fontSize": 20,
                "fontFamily": "Georgia, serif",
                "color": "#B8860B",
                "align": "center",
                "letterSpacing": 3
            },
            {
                "id": "date",
                "type": "text",
                "text": "Saturday, the Fourteenth of June",
                "x": 540, "y": 740,
                "fontSize": 34,
                "fontFamily": "Georgia, serif",
                "color": "#2C1810",
                "align": "center"
            },
            {
                "id": "year",
                "type": "text",
                "text": "Two Thousand and Twenty-Five",
                "x": 540, "y": 800,
                "fontSize": 28,
                "fontFamily": "Georgia, serif",
                "color": "#2C1810",
                "align": "center"
            },
            {
                "id": "time",
                "type": "text",
                "text": "at half past four in the afternoon",
                "x": 540, "y": 880,
                "fontSize": 26,
                "fontFamily": "Georgia, serif",
                "color": "#6B5744",
                "align": "center",
                "italic": True
            },
            {
                "id": "venue",
                "type": "text",
                "text": "The Grand Ballroom",
                "x": 540, "y": 980,
                "fontSize": 38,
                "fontFamily": "Georgia, serif",
                "color": "#2C1810",
                "align": "center"
            },
            {
                "id": "address",
                "type": "text",
                "text": "123 Rosewood Lane, New York",
                "x": 540, "y": 1040,
                "fontSize": 26,
                "fontFamily": "Georgia, serif",
                "color": "#6B5744",
                "align": "center"
            },
            {
                "id": "rsvp",
                "type": "text",
                "text": "Kindly reply by May 1st",
                "x": 540, "y": 1180,
                "fontSize": 22,
                "fontFamily": "Georgia, serif",
                "color": "#B8860B",
                "align": "center",
                "italic": True
            }
        ]
    },
    "modern_minimal": {
        "canvas": {"width": 1080, "height": 1350, "background": "#F8F8F6"},
        "elements": [
            {
                "id": "accent_left",
                "type": "shape",
                "shape": "rect",
                "x": 80, "y": 200, "width": 4, "height": 500,
                "fill": "#1A1A1A"
            },
            {
                "id": "label_top",
                "type": "text",
                "text": "YOU ARE INVITED",
                "x": 120, "y": 220,
                "fontSize": 14,
                "fontFamily": "Arial, sans-serif",
                "color": "#888888",
                "align": "left",
                "letterSpacing": 6
            },
            {
                "id": "names",
                "type": "text",
                "text": "Sophie\n& Luca",
                "x": 120, "y": 290,
                "fontSize": 96,
                "fontFamily": "Georgia, serif",
                "color": "#1A1A1A",
                "align": "left",
                "lineHeight": 1.1
            },
            {
                "id": "date_label",
                "type": "text",
                "text": "DATE",
                "x": 120, "y": 600,
                "fontSize": 12,
                "fontFamily": "Arial, sans-serif",
                "color": "#888888",
                "letterSpacing": 4
            },
            {
                "id": "date",
                "type": "text",
                "text": "September 20, 2025",
                "x": 120, "y": 630,
                "fontSize": 32,
                "fontFamily": "Georgia, serif",
                "color": "#1A1A1A",
                "align": "left"
            },
            {
                "id": "venue_label",
                "type": "text",
                "text": "VENUE",
                "x": 120, "y": 710,
                "fontSize": 12,
                "fontFamily": "Arial, sans-serif",
                "color": "#888888",
                "letterSpacing": 4
            },
            {
                "id": "venue",
                "type": "text",
                "text": "Villa Rosata\nFlorenze, Italy",
                "x": 120, "y": 740,
                "fontSize": 32,
                "fontFamily": "Georgia, serif",
                "color": "#1A1A1A",
                "align": "left",
                "lineHeight": 1.3
            },
            {
                "id": "footer",
                "type": "text",
                "text": "RSVP by August 1 · hello@sophieandluca.com",
                "x": 120, "y": 1280,
                "fontSize": 16,
                "fontFamily": "Arial, sans-serif",
                "color": "#888888",
                "letterSpacing": 1
            }
        ]
    },
    "garden_romance": {
        "canvas": {"width": 1080, "height": 1350, "background": "#F0F4EC"},
        "elements": [
            {
                "id": "corner_tl",
                "type": "text",
                "text": "✿",
                "x": 80, "y": 70,
                "fontSize": 60,
                "color": "#6B8F5E",
                "align": "left"
            },
            {
                "id": "corner_tr",
                "type": "text",
                "text": "✿",
                "x": 940, "y": 70,
                "fontSize": 60,
                "color": "#6B8F5E",
                "align": "left"
            },
            {
                "id": "corner_bl",
                "type": "text",
                "text": "✿",
                "x": 80, "y": 1220,
                "fontSize": 60,
                "color": "#6B8F5E",
                "align": "left"
            },
            {
                "id": "corner_br",
                "type": "text",
                "text": "✿",
                "x": 940, "y": 1220,
                "fontSize": 60,
                "color": "#6B8F5E",
                "align": "left"
            },
            {
                "id": "script_header",
                "type": "text",
                "text": "With joy we invite you to celebrate",
                "x": 540, "y": 200,
                "fontSize": 28,
                "fontFamily": "Georgia, serif",
                "color": "#5A7A4A",
                "align": "center",
                "italic": True
            },
            {
                "id": "the_wedding",
                "type": "text",
                "text": "the wedding of",
                "x": 540, "y": 270,
                "fontSize": 22,
                "fontFamily": "Georgia, serif",
                "color": "#7A9A6A",
                "align": "center",
                "italic": True
            },
            {
                "id": "name1",
                "type": "text",
                "text": "Isabella",
                "x": 540, "y": 360,
                "fontSize": 100,
                "fontFamily": "Georgia, serif",
                "color": "#2D4A1E",
                "align": "center"
            },
            {
                "id": "and_symbol",
                "type": "text",
                "text": "&",
                "x": 540, "y": 490,
                "fontSize": 72,
                "fontFamily": "Georgia, serif",
                "color": "#6B8F5E",
                "align": "center",
                "italic": True
            },
            {
                "id": "name2",
                "type": "text",
                "text": "Oliver",
                "x": 540, "y": 580,
                "fontSize": 100,
                "fontFamily": "Georgia, serif",
                "color": "#2D4A1E",
                "align": "center"
            },
            {
                "id": "floral_divider",
                "type": "text",
                "text": "~ ~ ~",
                "x": 540, "y": 720,
                "fontSize": 32,
                "color": "#6B8F5E",
                "align": "center"
            },
            {
                "id": "date",
                "type": "text",
                "text": "July 12, 2025",
                "x": 540, "y": 800,
                "fontSize": 42,
                "fontFamily": "Georgia, serif",
                "color": "#2D4A1E",
                "align": "center"
            },
            {
                "id": "time",
                "type": "text",
                "text": "5:00 in the Evening",
                "x": 540, "y": 870,
                "fontSize": 28,
                "fontFamily": "Georgia, serif",
                "color": "#5A7A4A",
                "align": "center",
                "italic": True
            },
            {
                "id": "venue",
                "type": "text",
                "text": "The Botanical Garden Estate",
                "x": 540, "y": 960,
                "fontSize": 36,
                "fontFamily": "Georgia, serif",
                "color": "#2D4A1E",
                "align": "center"
            },
            {
                "id": "address",
                "type": "text",
                "text": "Willow Grove, California",
                "x": 540, "y": 1015,
                "fontSize": 26,
                "fontFamily": "Georgia, serif",
                "color": "#5A7A4A",
                "align": "center"
            },
            {
                "id": "rsvp",
                "type": "text",
                "text": "Please RSVP by June 1st",
                "x": 540, "y": 1160,
                "fontSize": 22,
                "fontFamily": "Georgia, serif",
                "color": "#6B8F5E",
                "align": "center",
                "italic": True
            }
        ]
    }
}