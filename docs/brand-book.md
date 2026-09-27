# Lyre Restaurant & Café — Brand Book & Website Production Specification

**Prepared:** 27 September 2026 · **Prepared by:** Nisham Sajjad (website proposal) · **Status:** Research draft for owner review
**Prototype:** `index.html` in this repository (hero video: `assets/video/bodugola-signature-*.mp4`)

---

## How to read this document

Every important claim carries a confidence marker:

| Marker | Meaning |
|---|---|
| 🟢 **VERIFIED** | Seen directly on an official Lyre channel (Facebook page, Linktree, Lyre's own posts/reel) or in the company data supplied for this project |
| 🟡 **INFERRED** | Supported by third-party sources (Tripadvisor review titles, listing descriptions, aggregator snippets) or reasoned from evidence. Needs owner confirmation before publishing as fact |
| 🔴 **UNKNOWN** | Not found. **REQUIRES CONFIRMATION FROM RESTAURANT** |

### Research limits (read first)

- Tripadvisor, Mindtrip, X (twitter.com/x.com), White Harp Inn's website, Instagram and Facebook pages **could not be opened directly** from the research environment (network policy). Facts from those sites come from **search-engine result titles and snippets** and the **screenshots supplied by the client**, so they're marked 🟡 unless a screenshot shows them.
- The **X reference video** (`x.com/KrevixAi/status/2089970183674663188`) could not be loaded. The hero video was built in the common "AI product ad" style that link points to (macro push-ins, a light sweep, bold kinetic type, a logo end card), using only Lyre's real photography. Compare it with the reference yourself and adjust if needed (see §33).
- Google Maps listing and reviews could not be opened. Ratings quoted below come from an aggregator snippet (🟡).
- The menu and prices come from the **company data file supplied by the client** (`lyre-website-prototype.html`, which reproduces the printed menu). Treat as 🟢 for "was on the menu", 🟡 for "is current".

---

## 1. Executive Summary

Lyre (publicly "Lyre Restaurant & Café", "Café Lyre", Instagram "Lyre Cafe with Karaoke Lounge") is a casual, mid-priced beachfront café-restaurant on Beach Road, Hulhumalé. It serves Maldivian breakfasts (mashuni, roshi), burgers, kottu, Asian rice and noodle plates, pasta and grills, plus a long list of shakes, juices, mocktails and coffee. Recently it added **private karaoke rooms (10 AM – 2 AM)** and a shisha lounge. 🟢 (Linktree, Facebook, menu data)

Its one clearly ownable product is the **Bodugola ("The Giant Burger")**: a 2 kg beef burger, MVR 500, pre-order only. Guests describe it as "the biggest burger on the island". 🟢 menu / 🟡 review snippet. The second strongest asset is its **visual identity**: a confident red wordmark with an accent over the "y", used on bold red-background food photography and campaign-style posts ("LAYERS, BOLD TASTE", "GOURMET PERFECTION", the torn-paper pizza hands). 🟢

Lyre has **no website**. Its information is scattered across Facebook, Instagram (possibly two accounts), Linktree, a Google Drive menu PDF and Google Maps. Public ratings are middling (🟡 Google ≈3.8 from 42 reviews; Tripadvisor ≈3.4). Recurring praise covers burgers, food quality and the beach view; recurring complaints cover slow service and prices. 🟡

**Recommendation:** a single-page, mobile-first site with anchor sections (plus a dedicated `/menu` route when built for production). The main conversion is a **phone call or WhatsApp message** for karaoke bookings and Bodugola pre-orders, with "See the menu" and "Get directions" as secondary actions. Lead with the Bodugola video and the "Lyre is the place to be!" line. Do not use ratings as social proof yet.

---

## 2. Restaurant Profile

### 2.1 Brand identity

| Field | Finding | Confidence | Source |
|---|---|---|---|
| Official / public name | "Lyre Restaurant & Café" | 🟢 | Linktree page title |
| Other names in use | "Café Lyre" (Facebook address line), "Lyre" (Facebook page, posts), "Lyre Cafe with Karaoke Lounge" (Instagram name, via search), "Lyre Restaurant & Karaoke" (Mindtrip listing) | 🟢/🟡 | Facebook, Instagram search result, Mindtrip snippet |
| Tagline | "Lyre is the place to be!" / "is the place to be!" | 🟢 | End card of Lyre's own carrot-juice reel (supplied video) |
| Campaign lines | "LAYERS, BOLD TASTE", "GOURMET PERFECTION.", "Fresh, cheesy, and impossible to resist." | 🟢 | Facebook photo grid & 9 Sep post (screenshots) |
| Category | Café & restaurant with karaoke rooms and shisha lounge | 🟢 | Linktree, Instagram name, menu |
| Cuisine | Maldivian breakfast + international comfort food (burgers, sandwiches, pasta), Asian (nasi goreng, bami goreng, honey sesame chicken), Sri Lankan-style kottu, grills | 🟢 menu | Company data |
| Restaurant type | Casual, full-service, dine-in + outdoor seating | 🟢 | Facebook "Services: Outdoor seating · Dine-in" |
| Price positioning | Mid-range for Hulhumalé: most plates MVR 75–135, drinks MVR 19–89, Mixed Grill MVR 220, Bodugola MVR 500; +8% GST +10% service | 🟢 | Menu data |
| Location | Lot 11075, Beach Road (Kaani Magu), Hulhumalé, Malé City | 🟢 | Facebook post 9 Sep; Facebook About |
| Years operating | Reviewed on Tripadvisor since at least 2016 | 🟡 | Tripadvisor review "Best burgers in town" (review ID range dates to 2016) |
| Branches | One known location | 🟡 | No other branch found |
| Ownership | Facebook lists contact email `accounts@vtravelsmaldives.com`, which suggests a link to V Travels Maldives | 🟡 | Facebook About screenshot. **Do not publish this email** |
| History | Earlier reviews describe "Café Lyre" as downstairs from / part of **The White Harp Beach Hotel / White Harp Inn** on Beach Road | 🟡 | Tripadvisor review & photo titles via search |
| Milestones | "*New* Lyre Karaoke Rooms – 10AM to 02AM" | 🟢 | Linktree |

**Name story (🟡 inferred):** a lyre is a harp-family instrument. The café's historical home is the *White Harp* hotel, so the name is almost certainly a deliberate pairing. This gives the brand a free, authentic motif (strings, music) that fits the karaoke rooms. **Confirm the story with the owner before using it in copy.**

### 2.2 "Who is this restaurant?" (evidence-based narrative)

> Lyre is the red-branded café on Hulhumalé's Beach Road where the day starts with mashuni and roshi and ends in a private karaoke room at 2 AM. It's been feeding the beach road crowd for years with burgers, kottu, nasi goreng and a long menu of shakes and fresh juices, and it's the only place on the island that will build you a two-kilo burger if you call ahead. Casual, loud in colour, easy on the wallet, and right by the sea.

---

## 3. Business Model

| Revenue line | Evidence | Confidence |
|---|---|---|
| Dine-in food (breakfast, all-day) | Menu chapters "The Sunrise", "This & That", "Kottu Gang", "Small & Light", "The Last Meal" | 🟢 |
| Beverages (70+ items) | Thick Shakers, Mocktails, Fresh Chilled, Hot Stuff, Others | 🟢 |
| Pre-order centrepiece | Bodugola MVR 500, pre-order | 🟢 |
| Private karaoke rooms | Linktree "*New* Lyre Karaoke Rooms – 10AM to 02AM" (PDF) | 🟢 |
| Shisha | Karaoke/shisha lounge positioning; flavours and prices unknown | 🟡 |
| Delivery | No evidence on delivery platforms | 🔴 |
| Table reservations | No booking system found | 🔴 |
| Events / group bookings | Karaoke implies groups; no event packages found | 🔴 |

---

## 4. Market Positioning

| Axis | Position | Confidence |
|---|---|---|
| Affordable / mid / premium | **Mid-range** (plus 18% tax + service on top) | 🟢 |
| Casual / formal | **Casual** | 🟢 |
| Local / international | **Both:** Maldivian breakfast + international comfort food | 🟢 |
| Family / couples / groups | **Groups & friends** (karaoke, sharing burger); couples (beach view); families plausible | 🟡 |
| Fast casual / full service | **Full service** (service charge applies) | 🟢 |
| Everyday / occasion | **Everyday**, with occasion moments (Bodugola, karaoke nights) | 🟡 |
| Food / experience | **Both:** food-led by day, experience-led by night | 🟡 |
| Local / tourist | **Mainly local**, with guesthouse tourists on Beach Road | 🟡 |
| Traditional / modern | **Modern** branding, traditional breakfast | 🟢 |
| Mass / niche | **Mass market** | 🟡 |

### Brand positioning statement *(strategic interpretation, not an official Lyre statement)*

> For friends, families and Beach Road visitors in Hulhumalé, **Lyre** is the beachfront café that takes you from a Maldivian breakfast to a private karaoke room in one place, because it serves mashuni in the morning, burgers and kottu all day, 70+ drinks and karaoke until 2 AM, and it's home of the 2 kg Bodugola.

---

## 5. Customer Analysis

*Segments are inferred from the menu, services, location and public reviews. Not stereotypes; confirm with the owner.*

| Segment | Who | Why they visit | What they order | What matters | Discovery | Info needed before visiting | Helpful website features |
|---|---|---|---|---|---|---|---|
| **Friend groups / young adults** 🟡 | Locals in their late teens to 30s | Karaoke nights, hanging out late, shisha | Kottu, burgers, mocktails, shakes, shisha | Room availability, price per hour, open late, easy booking | Instagram, TikTok, word of mouth | Karaoke rates, capacity, how to book | One-tap WhatsApp booking with pre-filled message; clear 10 AM–2 AM hours |
| **Breakfast crowd / residents** 🟡 | Hulhumalé residents, workers before shifts | Maldivian breakfast by the beach | Mashuni, roshi, kulhimas, tea, Teh Trik | Opening time, price, speed | Walk-by, Facebook | What time breakfast starts | Opening hours (🔴 needed), "The Sunrise" menu tab |
| **Celebration / challenge groups** 🟢/🟡 | Birthdays, teams, groups of friends | The Bodugola | Bodugola, Mixed Grill, Mix Kottu | Pre-order notice, serves how many | Instagram reels, friends | Notice time, how many people it feeds | Bodugola feature + WhatsApp pre-order |
| **Beach Road visitors / guesthouse tourists** 🟡 | Tourists staying on Hulhumalé before or after flights | Convenient beachfront meal, sunrise view | Burgers, juices, pasta, Caesar salad | English menu, prices, location, open now | Google Maps, Tripadvisor | Directions, price, is it open | Menu with prices, map button, English copy |
| **Families** 🟡 | Local families at weekends | Beach outing | Nasi goreng, pasta, fries, ice cream, milkshakes | Kid-friendly items, seating | Facebook | Seating, outdoor area | Menu filters, seating info |
| **Delivery customers** 🔴 | Unknown | — | — | — | — | — | Only if Lyre confirms delivery |

---

## 6. Customer Psychology

| Customer question | Website answer | Status |
|---|---|---|
| What food do they serve? | Full tabbed menu with prices | 🟢 |
| How much does it cost? | Prices in MVR plus a clear note: "+8% GST & 10% service charge" | 🟢 |
| Where is it? | Lot 11075, Beach Road, Hulhumalé + "Get directions" | 🟢 |
| Is it open now? | Live "Karaoke open now" status (Maldives time). Café hours needed | 🟢 karaoke / 🔴 café |
| Can I reserve a table? | "Call or WhatsApp" once confirmed | 🔴 |
| Can I book karaoke? | Yes. WhatsApp or call 949-9969 | 🟢 |
| Do they deliver? | Unknown | 🔴 |
| Is it halal? | Maldives norm suggests yes, but **do not claim** | 🔴 |
| Signature dishes? | Bodugola, Kuda Gola, Lyre Special Nasi Goreng, Chicken Cheese Kottu, Mix Mashuni | 🟢 |
| Good for groups? | Karaoke rooms, Bodugola, Mixed Grill | 🟢 |
| Can I order on WhatsApp? | Number 949-9969 is shown; confirm it is on WhatsApp | 🔴 |
| Payment methods? | Unknown | 🔴 |
| Parking? | Unknown | 🔴 |
| Indoor/AC seating? | Reviews mention AC indoor seating and outdoor seating under palms | 🟡 |

---

## 7. Menu & Product Analysis

Source: company data (printed menu reproduction). Prices in MVR, before 8% GST + 10% service charge. "Pick" = marked as a Lyre pick on the printed menu. **Current?** = 🟡 for all rows until the owner confirms.

### 7.1 Food

| Category | Item | Description | Price | Signature? | Popularity evidence | Photo |
|---|---|---|---|---|---|---|
| The Sunrise | French Toast | With egg of your choice and sausage | 95 | | Photo posted | ✅ |
| The Sunrise | Pancakes | With a choice of egg & sausage | 95 | Pick | | |
| The Sunrise | Mix Mashuni | Three types of mashuni with huni roshi or roshi | 95 | ★ | Photo posted | ✅ |
| The Sunrise | Kulhimas | With huni roshi or roshi | 80 | | | |
| The Sunrise | Rihaakuru | With huni roshi or roshi | 80 | | | |
| The Sunrise | Mashuni | With huni roshi or roshi | 75 | | | |
| The Sunrise | Valhomas Mashuni | With huni roshi or roshi | 80 | | Photo posted | ✅ |
| The Sunrise | Fathu Mashuni | With huni roshi or roshi | 80 | | | |
| The Sunrise | Baraboa (Pumpkin) Mashuni | With huni roshi or roshi | 80 | | | |
| This & That | Lyre Special Nasi Goreng | Fried egg, prawn, crackers, slaw (from photo) | 120 | ★ (named after Lyre) | Photo posted | ✅ |
| This & That | Meatball Spaghetti | | 125 | | | |
| This & That | Bamigoreng | | 120 | | | |
| This & That | Spaghetti Alfredo | Seafood | 135 | | | |
| This & That | Meatball and Mash | | 120 | | | |
| This & That | Tuna Steak | With sautéed vegetables | 125 | | | |
| This & That | Creamy Spaghetti | Chicken | 105 | | "Spaghetti and Broccoli in cream sauce, served with garlic bread" post, 1 Jan 2024 | ✅ |
| This & That | Baked Spicy Rice | Greens, chicken / beef | 120 | Pick | | |
| This & That | Honey Sesame Chicken | With steamed rice | 105 | Pick | Photo posted | ✅ |
| This & That | **Kuda Gola** | Beef burger with salad, fries & hot sauce | 125 | Pick ★ | "Best burgers in town" review title | ✅ |
| This & That | The Rooster | Chicken burger with salad, fries & hot sauce | 115 | Pick | | |
| This & That | **Bodugola a.k.a. The Giant Burger** | 2 kg beef burger with fries & salad · pre-order | 500 | Pick ★★ | "Biggest burger on the island", review snippet | ✅ |
| This & That | Madam Sandwich | Chicken / beef / tuna | 90 | Pick | | |
| This & That | Chicken Chop | | 115 | | | |
| This & That | Chicken Sub | | 90 | | | |
| This & That | Beef Sub | | 110 | | | |
| This & That | Sandwich Chicken / Beef | With salad, fries & hot sauce | 90 | | | |
| This & That | Mixed Grill | Seafood, beef, chicken in black pepper sauce & garlic bread | 220 | Pick | Photo posted | ✅ |
| This & That | Broccoli & Beef Stir Fry | With steamed rice | 125 | | | |
| Kottu Gang | Chicken Cheese Kottu | | 110 | Pick ★ | Photo posted | ✅ |
| Kottu Gang | Chicken Kottu | | 100 | | | |
| Kottu Gang | Beef Kottu | | 110 | | | |
| Kottu Gang | Mix Kottu | | 115 | | Tripadvisor photo "Tuna Kottu" suggests kottu is long-standing 🟡 | |
| Small & Light | Green Salad | Chicken on request | 100 | | | |
| Small & Light | Beef & Fries | | 95 | | | |
| Small & Light | Cheese & Fries | | 95 | | | |
| Small & Light | Caesar Salad | Romaine, croutons, parmesan, Caesar dressing | 120 | Pick | | |
| Small & Light | Onion Rings | | 50 | | | |
| The Last Meal | Nutella Sandwich | | 100 | Pick | | |
| The Last Meal | Fresh Fruits | Seasonal | 100 | | | |
| The Last Meal | Ice Cream Scoop | Chocolate, vanilla, strawberry | 60 | | | |

### 7.2 Drinks (70+)

| Group | Items (MVR) |
|---|---|
| Thick Shakers | Strawberry/Chocolate/Vanilla Milkshake 79 · Banana/Mango Milkshake 79 · Oreo Milkshake 89 · Ice Milo 89 · Ice Coffee 89 · Mixed Berry Blast 89 · Oatmeal with Papaya 69 · Creamy Espresso 33/67 |
| Mocktails | Mint & Lime 69 · **Passionfruit & Turmeric 69** (mentioned in Mindtrip snippet 🟡) · Mango Mania 89 · Strawberry Margarita 69 · Lady Blue 79 · Watermelon Breeze 79 · Pomegranate Bull 79 · Redbull Rooster 89 · Kanbulo 89 · Aloha 79 · Blueberry Mojito 59 · Ginger Lemonade 69 |
| Fresh Chilled | Orange & Pineapple 69 · Watermelon & Orange 59 · Passionfruit & Pineapple 69 · Beetroot 69 · Orange 59 · Watermelon 59 · Pineapple 59 · Passionfruit 69 · Lime 39 · **Carrot 59** (own promo reel 🟢) · Mixed Fruit 79 |
| Hot Stuff | Espresso 39 · Americano 49 · Cappuccino 59 · Café Mocha 69 · Hot Chocolate 69 · Hazelnut Latte 69 · Milk Tea 29 · Hot Milo 74 · Assorted Tea 19 · Teh Trik 33 |
| Others | Soda Gembira 45 · Ice Lemon Tea 45 · Granini 31 · Iced Milk 34 · Water 10/15 · Nuts 14 · Soft drinks 19 · Bitter Lemon 22 · Red Bull 59 · Beer 0% 59 |
| Shisha | 🔴 Flavours & prices |

### 7.3 Product observations

- **Most promoted (🟢 visual evidence):** carrot juice (dedicated reel + red-studio stills), layered green/pink drink ("LAYERS, BOLD TASTE"), pizza (9 Sep campaign), grilled fish/chicken plate ("GOURMET PERFECTION"), beach salad bowl, spaghetti & broccoli.
- ⚠️ **Pizza is heavily promoted on Facebook (Sep 2026) but is not on the supplied menu.** The menu data may be out of date, or pizza is new. 🔴 **Confirm.** The prototype shows the pizza only as a campaign image in the gallery, not as a menu item.
- ⚠️ **"Beef & Broccoli" / grilled fish plate in posts** are only partly matched on the menu (Broccoli & Beef Stir Fry 🟢; the grilled fish plate 🔴).
- **High-value items:** Bodugola (500), Mixed Grill (220), Spaghetti Alfredo (135).
- **Margins:** cannot be inferred reliably. Beverages and kottu are *typically* high-margin in the category (general industry pattern, 🟡); no Lyre data.
- **Combos / family meals / seasonal:** none found 🔴.

---

## 8. Signature Product Strategy

### Hero product

| | **Bodugola a.k.a. The Giant Burger** |
|---|---|
| Why it matters | Unique on the island (🟡 review snippet), pre-order drives WhatsApp contact, built for groups, the most "shareable" item |
| Photo | `assets/img/bodugola-web.webp` (Lyre's own) → **hero video** `assets/video/bodugola-signature-landscape.mp4` / `-portrait.mp4` |
| Placement | Hero video + chapter bar; first item on the Signature board; FAQ |
| Copy | "Two kilos. One burger." · "a.k.a. The Giant Burger. A 2 kg beef burger with fries and salad. Pre-order only." · "Order ahead. Bring backup." |
| CTA | **Pre-order on WhatsApp** (pre-filled: "Hi Lyre! I'd like to pre-order a Bodugola for __ people on __ at __.") |

### Secondary products

| Product | Why | Photo | Copy | CTA |
|---|---|---|---|---|
| Kuda Gola (MVR 125) | Everyday burger; "Best burgers in town" review | `kuda-gola.webp` | "Our beef burger with salad, fries and hot sauce." | See the menu |
| Lyre Special Nasi Goreng (120) | Carries the brand name | `nasi-goreng.webp` | "The one with our name on it." | See the menu |
| Chicken Cheese Kottu (110) | Kottu is a Maldivian favourite, and it's a Lyre pick | `chicken-cheese-kottu.webp` | "Kottu and chicken under a blanket of cheese sauce." | See the menu |
| Mix Mashuni (95) | Local breakfast identity | `mix-mashuni.webp` | "Three types of mashuni with huni roshi or roshi." | See The Sunrise menu |
| Fresh Chilled Carrot (59) | Lyre's own promo reel | `carrot-juice-reel.mp4` | "Vibrant layers, bold taste." | See drinks |

### Supporting products
Honey Sesame Chicken, Mixed Grill, French Toast, Creamy Spaghetti, Mango Mania, Passionfruit & Turmeric, Oreo Milkshake, Teh Trik.

---

## 9. USP & Differentiation

### Verified USPs 🟢
1. **Bodugola, the 2 kg burger** (menu, pre-order).
2. **Private karaoke rooms, 10 AM – 2 AM daily** (Linktree).
3. **Maldivian breakfast + international menu under one roof** (menu).
4. **70+ drinks** (menu count).
5. **Beach Road location with outdoor seating** (Facebook).
6. **Bold red brand** that is recognisable across posts (visual audit).

### Possible positioning opportunities 🟡
- "Sunrise to singalong": the only Beach Road spot doing breakfast *and* late-night karaoke (needs café opening hours).
- Sunrise views (Tripadvisor review title "This is where u can watch sunrise").
- Long-standing Beach Road favourite since at least 2016 (confirm founding year).
- The lyre / White Harp name story (confirm).

### Claims we should NOT make 🔴
- "Best burger in the Maldives" / "#1" / "award-winning"
- "Halal certified", "fresh daily", "locally sourced", "organic"
- "Biggest burger in the Maldives" (review wording only; not verified)
- Any star rating or review count (current ratings are middling and unverified)
- "Fast service" (reviews say otherwise)
- Delivery, table reservations, payment methods, parking, before confirmation

---

## 10. Competitor Analysis (Hulhumalé)

*Source: search result listings (Tripadvisor, Wanderlog, Evendo, My Maldives Guide). Websites and ordering details were not verifiable in this session and are marked 🔴. Not ranked.*

| Venue | Cuisine | Price | Positioning / style | Website / ordering / reservation | Notes |
|---|---|---|---|---|---|
| Red Snapper & Coffee Beans | Café, breakfast, sandwiches, pasta | Mid | Beachside, remote-work friendly | 🔴 | Frequently listed as a top Hulhumalé café |
| Zaatar Cafe | Middle Eastern | Mid | Next to the public beach | 🔴 | Cuisine-led niche |
| Family Room Coffee | Coffee, burgers, salads | Mid | Self-service ordering, outdoor seating near the beach | 🔴 | Direct overlap on burgers |
| Cloud Signature | Artisan coffee, pastries | Mid–premium | Rooftop café at Grand Ocean Hotel | 🔴 | View-led |
| Thai Palace | Thai | Mid | Traditional, well-presented | 🔴 | |
| Dinemore Hulhumalé | Burgers / casual | Mid | Beachfront | 🔴 | Direct overlap |
| Rivo Lounge & Karaoke | Karaoke & shisha lounge | 🔴 | Private karaoke lounge on Beach Road | Instagram @rivo.mv | **Direct karaoke competitor** |
| Kanneiy Baa | Karaoke & sheesha | 🔴 | Lounge | 🔴 | Karaoke competitor |
| HH Lounge & Restaurant | South Indian + hookah + karaoke | 🔴 | Food + karaoke combo | 🔴 | Closest model to Lyre |

**Category patterns (🟡):** Instagram-first marketing; menus shared as images or PDFs; booking by phone/DM; few proper websites; karaoke venues market to night crowds and cafés to day crowds, rarely both.

**Differentiation opportunities:**
1. A real, fast website with a **text menu and prices** (most rely on PDFs and images).
2. **Day-to-night story** (breakfast → karaoke) that no single competitor tells.
3. **A signature "event" product** (Bodugola) with a pre-order flow.
4. **A distinctive red visual identity**, stronger than the typical beige café aesthetic.

---

## 11. Brand DNA

### 11.1 Brand personality (7 traits)

| Trait | Why it fits (evidence) |
|---|---|
| **Bold** | Saturated red backgrounds, all-caps campaign lines, a 2 kg burger |
| **Playful** | Torn-paper pizza hands, "Kuda Gola" / "Bodugola" / "The Rooster" / "Madam Sandwich" / "Kottu Gang" naming |
| **Local** | Dhivehi dish names (mashuni, roshi, kulhimas, rihaakuru, bodu = big, kuda = small), Beach Road address |
| **Social** | Karaoke rooms, sharing plates, group burger |
| **Warm** | Casual café, beach setting, "is the place to be!" invitation |
| **Modern** | Studio food photography, clean wordmark, Linktree/PDF digital habits |
| **Energetic** | Open till 2 AM, 70+ drinks, bright red |

### 11.2 Brand archetype

**Primary: The Everyman (Regular Guy/Gal)**, with a **Jester** streak.
- *Why:* mid-range prices, local breakfast, a place "to be" with friends, not a place to impress. The Jester shows up in the naming (Kuda/Bodu Gola, Kottu Gang), the giant burger and karaoke.
- *Website:* approachable, clear prices, no luxury affectations, a few playful moments (the "Two kilos. One burger." video, flickering karaoke headline).
- *Photography:* real plates, bold colour backdrops, hands and people having fun; no staged fine-dining minimalism.
- *Copywriting:* short, friendly, a little cheeky ("Order ahead. Bring backup."), never pompous.

---

## 12. Brand Voice

**Tone:** friendly · confident · playful · local · short.

Evidence: "Fresh, cheesy, and impossible to resist. 🤤🍕" · "Creamy delight! Our Spaghetti and Broccoli in cream sauce, served with garlic bread, is a pasta dream by the shore." · "LAYERS, BOLD TASTE" · "is the place to be!"

| DO | DON'T |
|---|---|
| "Two kilos. One burger." | "Indulge in our exquisite culinary masterpiece." |
| "Grab the mic." | "Experience unparalleled entertainment." |
| "Mashuni, kulhimas and rihaakuru with warm roshi." | "Authentic traditional Maldivian gastronomy." |
| Use Dhivehi dish names as-is | Translate or over-explain local dishes |
| "Call or WhatsApp to book your slot." | "Kindly contact our reservations team." |
| Emoji on social only | Emoji in website headings |

---

## 13. Visual Identity (audit)

| Element | Observation | Confidence |
|---|---|---|
| Logo | Wordmark "Lýre": geometric, thin-stroke sans with a long stem on the "L", an acute accent over the "y", and a looped "r/e". Used white-on-red in a circle (avatar, Linktree) and red-on-white on posts | 🟢 |
| Logo file | Only a **392×447 px white PNG** available (`assets/img/logo-white.png`) | 🟢 / 🔴 need vector |
| Colours | Lyre red (#EA1D3C measured from the logo circle), deeper red studio backdrops (#E0202B–#AE161E), white, dark red–maroon gradient on Linktree (#BD1302 → #820314); violet/purple for karaoke graphics | 🟢 measured from screenshots (estimates) |
| Typography on posts | High-contrast **serif, all caps** ("LAYERS, BOLD TASTE", "GOURMET PERFECTION.") in white on red | 🟢 |
| Photography | Two families: (a) **red-studio product shots** with hard directional light (carrot juice, layered drink, fish plate); (b) **top-down/three-quarter plated food** on speckled grey stoneware on dark granite or wood | 🟢 |
| Campaign ideas | Torn-paper "breakthrough" (pizza hands), beach-backdrop compositing (salad on beach) | 🟢 |
| Signboard, interior, exterior, uniforms, packaging | Not found | 🔴 |

**Existing visual language:** *Loud red, clean white, serif caps, food shot close and saturated. Confident rather than delicate.* The website should amplify this. It should not "elevate" it into beige minimalism.

---

## 14. Color System

*Hex values measured from supplied screenshots are estimates; confirm against the original logo file.*

| Role | Name | HEX | RGB | Usage |
|---|---|---|---|---|
| **Primary** | Lyre Red | `#EA1D3C` (logo) → web `#DD1638` | 234,29,60 → 221,22,56 | Hero, drinks band, footer, logo circle. Web value is 5% deeper so cream text passes 4.69:1 |
| **Secondary** | Deep Red | `#B80F2E` | 184,15,46 | Buttons, headings on cream, prices, frames. White on it = 6.68:1; it on cream = 5.89:1 |
| **Accent** | Karaoke Violet | `#7B2FD0` | 123,47,208 | Karaoke section only (from the karaoke graphic). White on it = 6.65:1 |
| Accent 2 | Wine | `#5E1628` | 94,22,40 | Visit section, gradients, dark surfaces |
| Accent 3 | Carrot | `#FF7A1A` | 255,122,26 | Tiny highlights only (from the carrot reel) |
| **Background** | Cream | `#FBEFE0` | 251,239,224 | Default page ground |
| Background alt | Paper | `#FFF8EF` | 255,248,239 | Menu board, signature section, cards |
| **Text** | Ink | `#22161A` | 34,22,26 | Body text (15.47:1 on cream) |
| **Muted text** | Muted | `#6C5A5E` | 108,90,94 | Descriptions (5.68:1 on cream) |
| Lines | Sand | `#EBD6C6` | | Dividers |
| **CTA** | Deep Red | `#B80F2E` | | Primary buttons; hover `#9C0C26` |

**Gradients:** Linktree-style `linear-gradient(180deg,#BD1302,#820314)` for night/footer moments; karaoke `linear-gradient(135deg,#7B2FD0,#5E1628)`.
**Dark mode:** not recommended for launch. The brand *is* the red/cream contrast. If needed later, use Wine `#5E1628` / Ink as the ground with Lyre Red accents.
**Contrast rules:** never set body-size white text on `#EA1D3C` (4.43:1 fails AA for small text); use `#DD1638` or deeper.

---

## 15. Typography

| Role | Font | Weight | Size range | Letter-spacing | Line-height | Usage |
|---|---|---|---|---|---|---|
| **Display** | Playfair Display (Google Fonts, OFL) | 900 Black, uppercase | 56–150 px (clamp 11.5vw) | −0.01em | 0.86–0.95 | Hero, section titles. Matches Lyre's serif-caps posts |
| **Display italic** | Playfair Display Italic | 700 | 24–36 px | 0 | 1.2 | Tagline "is the place to be!", review quotes |
| **Heading** | Playfair Display | 900 | 20–34 px | 0 | 1.1 | Dish names, card titles (uppercase) |
| **Body** | Titillium Web (Google Fonts, OFL) | 400/600 | 15–19 px | 0 | 1.55 | Paragraphs, descriptions |
| **Button / label** | Titillium Web | 700, uppercase | 11–14 px | 0.1–0.12em | 1 | Buttons, eyebrows, pills, nav |

Load with `display=swap`, preconnect to fonts.gstatic.com, and subset to Latin. Fallbacks: `Georgia, 'Times New Roman', serif` / `system-ui, 'Segoe UI', Roboto, sans-serif`.

---

## 16. Photography Art Direction

**Mood (one line):** *Saturated, close and confident: hard warm light on bold red or dark stone, realistic food colour, shot like a campaign rather than a menu.*

| Type | Angle | Light | Background | Props | Composition | Colour temp | Crop | DOF | Editing |
|---|---|---|---|---|---|---|---|---|---|
| **Food, hero** | 3/4 (30–45°) or low side angle for burgers | Hard key light from upper left, strong shadows | Seamless Lyre red or dark wood/granite | Wooden tray, speckled grey stoneware (Lyre's own) | Product fills 60–80% of frame | Warm 4500–5000K | Tight, allow cut edges | Shallow (f/2.8–4) | +contrast, +vibrance, reds protected, no fake HDR |
| **Food, menu** | Top-down 90° | Soft window/softbox | Dark granite (existing) | Minimal | Centred plate | Neutral-warm | Square 1:1 | Deep | Consistent across menu |
| **Beverage** | Eye-level + macro | Backlight for glow, hard key | Lyre red studio | Straw, garnish, wooden tray | Glass centred, room above for type | Warm | 4:5 / 9:16 | Shallow | Keep juice colour true |
| **Interior** 🔴 | Eye-level, wide | Natural daylight + practicals | — | Real tables in use | Show seating & sea | Natural | 3:2 | Medium | Light touch |
| **Exterior** 🔴 | From Beach Road & beach side | Golden hour / sunrise | Signage visible | — | Signboard + palms | Warm | 16:9 | Deep | — |
| **People / karaoke** 🔴 | Candid, handheld | Room lighting + fill | Karaoke room | Mics, screens | Groups mid-song | Mixed/cool | 4:5 | Shallow | Keep grain, no retouching faces |
| **Hero video** | Macro push-ins, lateral slides | Existing photo + light sweep | Red panel / wine glow | — | Chaptered 01–04 beats | Warm | 16:9 desktop, 4:5 mobile | — | Film grain, vignette |

---

## 17. Graphic Design System

| Token | Spec |
|---|---|
| Border radius | 4 px for photos and frames (editorial, not "app-like"); 999 px for pills/buttons; 14 px only for the karaoke info card |
| Cards | Avoid generic cards. Use **framed boards**: 1.5 px Deep Red outer rule, 1 px 35%-opacity inner rule at 7 px inset, **lyre corner ornaments** (22 px) |
| Buttons | Pill, 46 px min height, uppercase Titillium 700 13 px, 0.1em tracking, 22 px side padding; primary Deep Red / Paper text; secondary Paper bg / Deep Red text; ghost = 2 px currentColor outline; hover lift −2 px + arrow slides 4 px |
| Shadows | Only on floating elements: plates `0 18px 40px rgba(94,22,40,.28)`, review stamp drop-shadow `0 20px 40px rgba(0,0,0,.4)` |
| Borders / dividers | 1 px Sand `#EBD6C6` between list rows; 1.5 px cream rules on red |
| Icons | 24 px line icons, 1.9 px stroke, round caps (phone, WhatsApp, pin, mic, Instagram) |
| Decorative shapes | Hand-drawn line doodles (burger, juice glass, mic, palm) at 50% cream on red; **stamp/perforated** review card; **arch** photo frame; **wave pattern** on cream sections (beach) |
| Patterns | Wave tile `80×40` in `#E9D3BE` |
| Image treatment | Circle-cropped floating plates rotated ±10°; arch tops (180 px radius) on drink reel |
| Hover | Dish rows reveal an arrow and swap the showcase image; gallery zoom 1.05 |
| Animation | Hero headline rises 28 px over 0.9 s staggered 60–80 ms; karaoke headline "neon flicker" every 6 s; all disabled under `prefers-reduced-motion` |

---

## 18. Digital Presence Audit

| Platform | Status | Activity | Quality | Opportunity |
|---|---|---|---|---|
| **Website** | ❌ None | — | — | Own the brand search; host menu, hours, booking |
| **Google Maps** | 🟡 Listed ("Lyre Restaurant & Karaoke"), ≈3.8★ / 42 reviews per aggregator | 🔴 | 🔴 Unverified | Claim & complete profile: hours, menu link, photos, website URL, reply to reviews |
| **Instagram** | 🟢 @lyre.mv ("Lyre Cafe with Karaoke Lounge"); also **@lyre.mvone01** (post dated 1 Jan 2024) | Active (screenshots) | High-quality food photography | 🔴 Confirm which handle is official; link bio to website |
| **Facebook** | 🟢 facebook.com/CafeLyre | Active (post 9 Sep) | Good posts; About section outdated (email, "Male" address) | Update About (address Lot 11075, website, hours) |
| **Linktree** | 🟢 linktr.ee/Lyre.mv: karaoke PDF, Google Drive menu, FB/IG/TikTok icons | Current | Functional, generic | Replace with website link or add website as first link |
| **TikTok** | 🟢 icon on Linktree | 🔴 | 🔴 | Confirm handle |
| **WhatsApp** | 🔴 Not confirmed that 949-9969 is on WhatsApp | — | — | Enable WhatsApp Business with catalogue |
| **Delivery** | 🔴 None found | — | — | Only if the business wants it |
| **Booking** | 🔴 Phone only | — | — | WhatsApp pre-filled messages (no booking software needed) |
| **Tripadvisor** | 🟡 Listed, ≈3.4★, #50 of 87 in Hulhumalé | Old reviews | Mixed | Claim listing, add photos, respond |

**Scattered information today:** address (FB About vs FB posts), menu (Google Drive PDF), karaoke hours (Linktree PDF), phone (FB), food photos (IG/FB), reviews (Google/Tripadvisor). The website should gather all of it in one place.

---

## 19. Customer Journeys

| # | Journey | Entry → Steps → CTA → Conversion | Friction removed |
|---|---|---|---|
| 1 | "I want to see the menu." | Instagram bio / Google → site → sticky bar "Menu" → tab "This & That" → sees price | No PDF download; prices visible; tax note visible |
| 2 | "I want to visit." | Google search → hero → sticky "Directions" → Google Maps | Address + map in two taps; hours shown (🔴 needs café hours) |
| 3 | "I want to reserve." | Karaoke section → "Book on WhatsApp" (pre-filled date/time/people) → Lyre confirms | No form to fill in; staff reply in a chat they already use. Table booking 🔴 |
| 4 | "I want to order food." | Menu → Bodugola "Pre-order" → WhatsApp | Delivery 🔴; dine-in pre-order only |
| 5 | "I found Lyre on Instagram." | IG bio link → hero video (same look as the feed) → Signature board → WhatsApp / Menu | The site continues the Instagram look; no visual break |

---

## 20. Website Strategy

- **Type:** single-page site (anchors), mobile-first, static HTML/CSS/JS. A separate `/menu` page is recommended in production for SEO.
- **Primary goal:** turn visitors into **calls and WhatsApp messages** (karaoke bookings, Bodugola pre-orders, visits).
- **Secondary goals:** menu views, directions taps, Instagram follows.
- **Principles:** real photos only; text menu with prices; every unknown fact shown as a visible `confirm` tag in the proposal and **removed or filled before launch**.

---

## 21. Information Architecture

| Page / section | Purpose | Target customer | Required content | Primary CTA | Secondary CTA |
|---|---|---|---|---|---|
| **Home** `/` | Brand + all key info | Everyone | Hero video, story, signatures, reviews, day, karaoke, menu, drinks, feed, visit | WhatsApp / Call | Menu, Directions |
| **Menu** `/menu` (or `#menu`) | Full text menu | Everyone | Tabs, prices, tax note | Call / WhatsApp | Directions |
| **Karaoke** `#karaoke` (→ `/karaoke` later) | Room bookings | Groups | Hours, rates 🔴, capacity 🔴, how to book | Book on WhatsApp | Call |
| **Visit** `#visit` | Location & practical info | Visitors | Address, phone, hours, map, FAQ | Get directions | WhatsApp |
| Not now | Order online, Catering, Events, Blog, Careers | — | No evidence of business need | — | — |

---

## 22. Homepage Blueprint

| # | Section | Purpose | Headline / copy | Image / video | CTA | Design | Animation | Mobile | Business objective |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Nav** (fixed, inset) | Wayfinding | Logo "LYRE" · Signatures · Menu · Karaoke · Visit | Logo in red circle | "Book a room" | Cream bar, 10 px radius, 12 px from top, over the red hero | Shadow on scroll | Logo + "☰ Menu" overlay; CTA hidden (sticky bar handles it) | Constant access to booking |
| 2 | **Hero** | State the thesis | Badge: live karaoke status · H1 "LYRE IS / THE PLACE / TO … BE!" · meta "Beach Road" / "Hulhumalé" | **Bodugola signature video** in a notched frame between "TO" and "BE!" | Chapter bar 01–04 · "Bodugola, The Giant Burger · 2 kg · MVR 500" · Pause · **Pre-order →** | Lyre red, line doodles, reference layout | Headline rise; video autoplay muted loop | 4:5 portrait video, chapters row on top of title/CTA | Signature product, pre-order leads |
| 3 | Proposal ribbon | Proposal-only notice | "Website proposal for Lyre… items marked confirm need the owner's input" | — | — | Ink bar | — | — | **Remove at launch** |
| 4 | **Intro ("soul")** | Who Lyre is | Pill "Café · Restaurant · Karaoke" · H2 "Maldivian mornings. Beachfront nights." · lede | Floating round plates (nasi goreng, mixed grill); 2 photos (Valhomas Mashuni MVR 80, Kuda Gola MVR 125) | — | Wave pattern, framed board with lyre corners | Plates straighten on hover | Single column | Positioning |
| 5 | **Signature plates** | Hero products | H2 "Signature plates" · pill "Lyre picks" · 5 dishes with price | Showcase image swaps on hover/focus; inset photo | "See the full menu →" | Framed menu board (reference) | Crossfade 0.35 s | Showcase above list | Drive menu + pre-order |
| 6 | **Reviews** | Social proof (honest) | Real Tripadvisor review titles: "Best burgers in town", "This is where u can watch sunrise" | Beach salad photo background | ← → | Perforated red stamp card (reference) | — | Arrows at bottom | Trust. **Owner to add approved Google reviews** |
| 7 | **Sunrise to singalong** | Day-to-night story | Morning / All day / Till 2 AM | 3 real photos | — | 3 columns | — | Stacked | Broaden occasions |
| 8 | **Karaoke** | Room bookings | "Grab the mic." · hours · rooms 🔴 · rate 🔴 · shisha 🔴 · 3 steps | — | Book on WhatsApp · Call | Violet→wine gradient, perspective grid | Neon flicker | Stacked | Bookings |
| 9 | **Menu** | Full menu | "The menu" · 7 tabs | Round thumbs on key items | — | Sticky tabs | — | Scrollable tabs | Conversion support |
| 10 | **Drinks** | Beverage range | "Vibrant layers, bold taste." · chips | **Lyre's own carrot-juice reel** (arch frame) + spaghetti photo | — | Red band | Reel plays only on screen | Stacked | Upsell drinks |
| 11 | **On the feed** | Social | "On the feed" | 6-tile gallery → Instagram | Follow @lyre.mv | Edge-to-edge grid | Zoom on hover | 3 columns | Followers |
| 12 | **Visit** | Practical | "Find us on Beach Road" · address · phone + copy · hours table · FAQ | Illustrated map → Google Maps | Get directions · WhatsApp | Wine section, paper card | — | Stacked | Footfall |
| 13 | **Footer** | Close | Logo · "is the place to be!" · Visit · Follow | — | — | Red | — | Stacked | Brand recall |
| 14 | **Sticky mobile bar** | Quick actions | Call · WhatsApp · Menu · Directions | — | Call (highlighted) | Ink bar | — | ≤760 px only | Calls |

---

## 23. Page-by-Page Specification

### Home — see §22.

### Menu page (`/menu`, production)
- **Objective:** a crawlable, fast text menu.
- **Hero:** red band, H1 "The Lyre menu", sub "40 plates, 70+ drinks. Prices in MVR, +8% GST & 10% service."
- **Categories:** The Sunrise · This & That · Kottu Gang · Small & Light · The Last Meal · Drinks (Thick Shakers, Mocktails, Fresh Chilled, Hot Stuff, Others) · Shisha 🔴.
- **Product rows:** number · name · description · protein tags · "Lyre pick" tag · MVR price; 60 px round thumbnail when a real photo exists.
- **CTA:** sticky bar (Call / WhatsApp); Bodugola row links to the pre-order.
- **Mobile:** horizontally scrollable sticky tabs, single-column rows.
- **SEO:** title "Menu & Prices | Lyre Restaurant & Café, Hulhumalé"; `Menu` schema with `MenuSection`/`MenuItem` + `offers.priceCurrency: MVR`.

### Karaoke (`#karaoke`, later `/karaoke`)
- **Objective:** room bookings. **Content:** hours 🟢; number of rooms, capacity, rate, minimum spend, song library, food packages 🔴. **CTA:** WhatsApp pre-filled. **SEO:** "Karaoke rooms in Hulhumalé | Lyre".

### Visit (`#visit`)
- Address, phone (selectable + copy), hours table, seating, payment 🔴, FAQ, map link, WhatsApp.

---

## 24. UX/UI System — Component Library

| Component | Purpose | Visual | Content | Interaction | Responsive |
|---|---|---|---|---|---|
| Navbar | Wayfinding | Cream inset bar on red | Logo, 4 links, CTA | Shadow on scroll | Burger overlay ≤1000 px |
| Menu overlay | Mobile nav | Full-screen red, huge serif links | Links + Call/WhatsApp | Esc closes, focus returns | — |
| Hero stage | Thesis | Split headline + notched video | H1, badge, meta | Video autoplay, chapters seek | Portrait video ≤760 px |
| Chapter bar | Video control | Dark glass bar | 01–04, title, pause, CTA | Seek, pause, active underline | Wraps to 2 rows |
| Framed board | Section container | Double rule + lyre corners | Any | — | Padding shrinks |
| Dish row | Signature list | Serif red name, muted desc, price | Name/desc/price | Hover/focus/tap swaps showcase | Full width |
| Showcase | Big dish image | Photo + inset + caption | — | Crossfade | 4:5 on top |
| Stamp review card | Testimonial | Perforated red card | Quote, source | Prev/next | Arrows move below |
| Day card | Story | Photo + label + title | — | — | Stacked |
| Karaoke info card | Booking info | Glass card | Hours, dl, steps | — | Stacked |
| Menu tabs | Navigation | Pills, sticky | 7 tabs | Arrow keys, remembers last tab | Scrollable |
| Menu row | Item | Grid row | — | — | Single column |
| Drink reel | Video | Arch-top frame | Carrot reel | Plays when visible | — |
| Gallery | Social | 6/3 column squares | IG images | Zoom | 3 columns |
| Visit card | Info | Paper card | Address, phone, hours, FAQ | Copy number, details/summary | Stacked |
| Map card | Directions | Illustrated SVG map | Pin | Opens Google Maps | — |
| Sticky bar | Quick actions | Ink bar, Call in red | 4 actions | — | ≤760 px only |
| Button | CTA | Pill | Label + icon | Lift + arrow slide | — |
| Confirm tag | Proposal marker | Dashed outline | "confirm …" | — | **Remove at launch** |

---

## 25. Mobile Strategy

- **Navigation:** logo + "☰ Menu" button → full-screen red overlay with Call and WhatsApp.
- **Sticky CTA bar** (bottom, safe-area aware): **Call** (red, primary) · WhatsApp · Menu · Directions.
- **Hero:** headline at 12.6vw, portrait 4:5 video (`-portrait.mp4`, 720×900, ~1.5 MB).
- **Menu:** sticky scrollable tabs under the nav; 44 px+ tap targets.
- **Images:** serve ≤640 px wide WebP on mobile; `loading="lazy"` below the fold.
- **Typography:** body 17 px, labels ≥11 px, display clamp.
- **Spacing:** sections 64 px vertical, 16 px side gutter.
- **Footer** padded 100 px so the sticky bar never covers content.

---

## 26. SEO Strategy (Local)

*No search-volume claims are made; keywords are chosen for relevance.*

| Item | Recommendation |
|---|---|
| Primary keyword | Lyre Hulhumalé |
| Secondary | Lyre café, Lyre restaurant Hulhumalé, Café Lyre Beach Road |
| Category + location | burger Hulhumalé, karaoke Hulhumalé, karaoke rooms Malé, Maldivian breakfast Hulhumalé, mashuni Hulhumalé, beachfront café Hulhumalé, kottu Hulhumalé |
| Product | Bodugola, giant burger Maldives, 2 kg burger |
| Meta title (home) | `Lyre Restaurant & Café · Beach Road, Hulhumalé` |
| Meta description | "Lyre Restaurant & Café on Beach Road, Hulhumalé. Beachfront burgers, Maldivian breakfast, kottu, 70+ drinks and private karaoke rooms 10 AM – 2 AM. Call 949-9969." |
| H1 | "Lyre is the place to be!" (visual split; screen-reader text completes it) |
| Schema | `Restaurant` (name, alternateName, address, telephone, servesCuisine, priceRange, sameAs, amenityFeature) ✅ in prototype; add `openingHoursSpecification` 🔴, `geo` 🔴, `Menu`, and `EntertainmentBusiness` for karaoke |
| Google Business Profile | Claim/verify; category "Café" + "Karaoke bar"; add website, menu URL, hours, 20+ photos, reply to reviews, weekly posts |
| Alt text | "[Dish] at Lyre, Hulhumalé" plus key ingredients; decorative images `alt=""` |
| NAP consistency | Use **exactly** "Lyre Restaurant & Café, Lot 11075, Beach Road, Hulhumalé, Maldives · +960 949 9969" everywhere (fix the Facebook About) |

---

## 27. Conversion Strategy

| Type | Action |
|---|---|
| **Primary CTA** | **WhatsApp 949-9969** (pre-filled messages for karaoke booking and Bodugola pre-order). 🔴 Confirm WhatsApp is active; otherwise make **Call** primary |
| Secondary CTA | See the menu · Get directions |
| Quick-action CTA | Call 949-9969 (tel link + visible selectable number + copy button) |
| Sticky mobile CTA | Call · WhatsApp · Menu · Directions |

Track: `tel:` clicks, `wa.me` clicks, Maps clicks, menu tab views (GA4 or Plausible events).

---

## 28. Content Requirements (inventory)

| Asset | Status |
|---|---|
| Restaurant description | 🟢 drafted (§31) |
| About / history | 🟡 needs founding year & name story |
| Menu descriptions | 🟢 from menu; 🟡 current? |
| USPs | 🟢 |
| FAQs | 🟡 drafted with gaps |
| Contact (phone) | 🟢 949-9969 |
| WhatsApp | 🔴 |
| Address | 🟢 Lot 11075, Beach Road, Hulhumalé |
| Café opening hours | 🔴 |
| Karaoke hours | 🟢 10 AM – 2 AM |
| Karaoke rates / rooms | 🔴 |
| Reservation policy | 🔴 |
| Delivery | 🔴 |
| Payment methods | 🔴 |
| Logo (vector) | 🔴 only 392 px white PNG |
| Hero video | 🟢 produced from Lyre photo (owner approval needed) |
| Signature dish photos | 🟢 Bodugola, Kuda Gola, Nasi Goreng, Kottu, Mashuni |
| Drinks | 🟢 carrot reel & stills; 🔴 layered drink hi-res |
| Desserts | 🔴 |
| Interior / exterior / staff / customers / karaoke rooms | 🔴 |
| Reviews to quote | 🟡 titles only; owner to approve Google reviews |

---

## 29. Image Requirements

| Section | Image required | Existing source | Recommended | Aspect | Priority | AI OK? |
|---|---|---|---|---|---|---|
| Hero | Signature product video | Bodugola photo → rendered video ✅ | Reshoot Bodugola as real video (macro, 4K, red studio) | 16:9 + 4:5 | P1 | Motion design OK; **food must stay real** |
| Intro | 2 round plates + 2 dishes | ✅ | Transparent cut-outs of plates | 1:1, 4:3 | P2 | Background removal OK |
| Signatures | 5 dishes | ✅ (Kuda Gola had caption text; cropped) | Clean originals without text | 4:5 | P1 | No |
| Reviews bg | Ambience | Beach salad ✅ | Real beachfront table shot | 16:9 | P2 | No |
| Day | Morning / day / night | ✅ | Night karaoke shot | 4:5 | P2 | No |
| Karaoke | Room photo | 🔴 | Karaoke room with group | 4:5 | **P1** | No |
| Drinks | Carrot reel ✅, layered drink | ✅ reel | Hi-res layered drink | 9:14 | P2 | No |
| Visit | Exterior/signboard | 🔴 | Storefront from Beach Road | 3:2 | **P1** | No |
| Logo | Vector | 🔴 | SVG / AI / PDF | — | **P1** | No (never redraw a real logo with AI) |
| OG image | Social share | Video poster ✅ | 1200×630 | 1.91:1 | P2 | — |

---

## 30. Technical Requirements

- **Stack:** static HTML/CSS/vanilla JS (as prototyped) or Astro/Next static export. Host on Netlify/Vercel/Cloudflare Pages with HTTPS.
- **Images:** WebP (AVIF optional), `width`/`height` set, `loading="lazy"` below fold, hero poster `fetchpriority="high"`; max 1600 px.
- **Video:** H.264 MP4 `+faststart`, muted, `playsinline`, poster; portrait cut on phones; pause button; no autoplay under reduced motion. Landscape 1.8 MB / portrait 1.5 MB.
- **Fonts:** 2 families, `display=swap`, preconnect; consider self-hosting subsets.
- **Core Web Vitals targets:** LCP < 2.5 s on 4G (poster image is the LCP), CLS < 0.1 (all media sized), INP < 200 ms.
- **Accessibility:** WCAG 2.2 AA contrast (validated §14), visible focus, keyboard tabs, Esc closes overlay, `aria-current` on chapters, alt text, reduced motion.
- **SEO:** schema.org JSON-LD, sitemap.xml, robots.txt, canonical, OG tags.
- **Security:** HTTPS, `rel="noopener"` on external links, no forms posting to third parties.
- **Analytics:** GA4 or Plausible with events: `call_click`, `whatsapp_click`, `directions_click`, `menu_tab_view`, `preorder_click`.

---

## 31. Website Content Draft

- **Hero H1:** LYRE IS THE PLACE TO BE!
- **Hero badge:** Karaoke open now · till 2 AM *(live)*
- **Hero video bar:** Bodugola · The Giant Burger · 2 kg · MVR 500 · [Pre-order →]
- **Intro H2:** Maldivian mornings. Beachfront nights.
- **Intro copy:** A beachfront café on Hulhumalé's Beach Road. Mashuni and roshi for breakfast, burgers and kottu all day, and private karaoke rooms until 2 AM.
- **About (for /about or footer):** Lyre has been on Hulhumalé's Beach Road since [REQUIRES RESTAURANT CONFIRMATION: founding year]. [REQUIRES RESTAURANT CONFIRMATION: name story]
- **Signature board:** see §8.
- **Reviews:** "Best burgers in town" / "This is where u can watch sunrise" (Tripadvisor review titles). [ADD OWNER-APPROVED GOOGLE REVIEWS]
- **Day H2:** Sunrise to singalong. "Same seat by the beach, three different moods."
- **Menu intros:** *The Sunrise*: Maldivian breakfast with huni roshi or roshi. *This & That*: burgers, rice, pasta and grills. *Kottu Gang*: chopped, fried, loaded. *Small & Light*: salads and sides. *The Last Meal*: something sweet.
- **Karaoke:** "Grab the mic. Private karaoke rooms for you and your crew, open 10 AM to 2 AM. Call or WhatsApp to book your slot."
- **Drinks:** "Vibrant layers, bold taste. Thick shakes, fresh juices and house mocktails. Seventy-plus ways to cool down on Beach Road."
- **Visit:** "Find us on Beach Road. Lot 11075, Beach Road, Hulhumalé, Maldives. 949-9969."
- **Footer:** "is the place to be!"

---

## 32. Owner Questionnaire

**Business**
1. What year did Lyre open? Is it connected to The White Harp hotel, and is that where the name "Lyre" comes from?
2. Is the email on Facebook (accounts@vtravelsmaldives.com) the right public contact, or should the site show another one?
3. Which name do you prefer in public: "Lyre Restaurant & Café", "Café Lyre" or "Lyre"?

**Menu**
4. Is the menu in the Google Drive link current? Please send the latest version.
5. Is pizza on the menu now (your 9 Sep post)? Which pizzas and at what prices?
6. How much notice does the Bodugola need, and how many people does it feed?
7. Shisha flavours and prices?
8. Are all dishes halal? May we say so?

**Ordering**
9. Do you deliver or take away? Through which apps?
10. Is 949-9969 on WhatsApp, and who answers it?

**Reservations**
11. Can guests book tables, or only karaoke rooms?
12. Karaoke: how many rooms, how many people each, price per hour or minimum spend?

**Branding**
13. Can you send the logo as a vector file (AI/SVG/PDF) and your brand colours/fonts?
14. Which Instagram account is official: @lyre.mv or @lyre.mvone01? What is your TikTok handle?

**Photography**
15. Can we photograph the interior, the exterior/signboard, the karaoke rooms and a real Bodugola?
16. Do you approve the Bodugola signature video made from your photo?

**Contact**
17. Café and kitchen opening hours for each day (breakfast start time)?
18. Payment methods (cash, card, bank transfer, BML)?
19. Is parking available nearby? Is there AC indoor seating?

**Website**
20. Which Google reviews may we quote on the site?
21. Who will update the menu and prices after launch?
22. Do you already own a domain (for example lyre.mv)?

**Future plans**
23. Any events, set menus, group packages or new branches coming up?

---

## 33. Brand Book Summary

| | |
|---|---|
| **Name** | Lyre Restaurant & Café (Café Lyre) |
| **Category** | Casual beachfront café-restaurant with private karaoke rooms & shisha |
| **Location** | Lot 11075, Beach Road, Hulhumalé, Maldives |
| **Positioning** | The Beach Road place for Maldivian breakfast, big burgers and late-night karaoke |
| **Personality** | Bold · Playful · Local · Social · Warm · Modern · Energetic |
| **Brand promise** | *Whatever time you come, Lyre is the place to be.* |
| **Target customers** | Friend groups, breakfast locals, celebration groups, Beach Road visitors, families |
| **USP** | 2 kg Bodugola · Karaoke rooms 10 AM–2 AM · Maldivian breakfast + international menu · 70+ drinks · Beach Road outdoor seating |
| **Voice** | Friendly, confident, short, a little cheeky; Dhivehi dish names as-is |
| **Visual identity** | Loud red + clean cream, serif caps, saturated close food photography, lyre-string corner ornaments |
| **Colour palette** | `#EA1D3C` logo red · `#DD1638` web red · `#B80F2E` deep red · `#FBEFE0` cream · `#FFF8EF` paper · `#22161A` ink · `#5E1628` wine · `#7B2FD0` karaoke violet |
| **Typography** | Playfair Display 900 caps / 700 italic · Titillium Web 400/600/700 |
| **Photography** | Hard warm light, red studio or dark stone, tight crops, true colour |
| **Graphic style** | Framed boards with lyre corners, perforated stamp cards, arch frames, wave pattern, line doodles |
| **Customer experience** | Find → see price → tap WhatsApp/Call → arrive on Beach Road |

---

## 34. Website Design System (developer summary)

```css
:root{
  /* colour */
  --red:#DD1638; --red-logo:#EA1D3C; --red-deep:#B80F2E; --red-hover:#9C0C26;
  --cream:#FBEFE0; --paper:#FFF8EF; --ink:#22161A; --muted:#6C5A5E; --line:#EBD6C6;
  --wine:#5E1628; --violet:#7B2FD0; --carrot:#FF7A1A;
  /* type */
  --display:'Playfair Display',Georgia,'Times New Roman',serif;
  --body:'Titillium Web',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  --fs-hero:clamp(56px,11.5vw,150px); --fs-h2:clamp(40px,6.4vw,76px);
  --fs-h3:clamp(20px,2.2vw,26px); --fs-body:17px; --fs-label:12.5px;
  /* spacing & layout */
  --gut:clamp(16px,4vw,40px); --section:clamp(64px,9vw,112px); --container:1200px;
  --radius-photo:4px; --radius-card:14px; --radius-pill:999px;
  /* motion */
  --ease:cubic-bezier(.2,.7,.2,1); --t-fast:.15s; --t-med:.35s; --t-slow:.9s;
}
/* breakpoints: 760px (mobile), 1000px (tablet) */
/* buttons: min-height 46px (sm 38px), padding 0 22px, uppercase 13px/700/.1em */
/* grid: 12-col mental model; signature board 1fr 1fr; day 3 cols; gallery 6→3 cols */
```

**Responsive rules:** ≤1000 px → burger nav, single-column menu, 3-col gallery. ≤760 px → portrait hero video, stacked sections, sticky bottom bar, headline 12.6vw.

---

## 35. MASTER WEBSITE-BUILD PROMPT

> Paste everything inside the box into an AI website builder.

```text
Build the official website for LYRE RESTAURANT & CAFÉ ("Café Lyre"), a casual, mid-priced beachfront
café-restaurant with private karaoke rooms on Beach Road, Hulhumalé, Maldives. The site must look like a
professionally commissioned site for THIS restaurant, not a template. DO NOT INVENT ANY FACT. Where a fact
is missing, show the exact placeholder in square brackets, e.g. [CONFIRM OPENING HOURS].

== IDENTITY ==
Name: Lyre Restaurant & Café. Tagline: "Lyre is the place to be!" (end card: "is the place to be!").
Address: Lot 11075, Beach Road, Hulhumalé, Maldives. Phone: 949-9969 (+960 949 9969).
WhatsApp: [CONFIRM WHATSAPP NUMBER — assume 949-9969 only after confirmation].
Instagram: @lyre.mv [CONFIRM OFFICIAL HANDLE]. Facebook: facebook.com/CafeLyre. Linktree: linktr.ee/Lyre.mv.
TikTok: [CONFIRM HANDLE]. Karaoke rooms: 10 AM – 2 AM daily. Café hours: [CONFIRM OPENING HOURS].
Seating: outdoor + dine-in. Payment: [CONFIRM PAYMENT METHODS]. Delivery: [CONFIRM]. Table booking: [CONFIRM].
Prices are in MVR and subject to 8% GST and 10% service charge. Founded: [CONFIRM YEAR].

== PERSONALITY & VOICE ==
Bold, playful, local, social, warm, modern, energetic. Archetype: Everyman with a Jester streak.
Copy: short sentences, friendly, confident, slightly cheeky. Keep Dhivehi dish names (mashuni, roshi,
huni roshi, kulhimas, rihaakuru, Kuda Gola, Bodugola). No luxury clichés ("exquisite", "unparalleled",
"culinary journey"). No emoji in headings. No superlatives or awards. No ratings.

== POSITIONING (internal) ==
For friends, families and Beach Road visitors in Hulhumalé, Lyre is the beachfront café that takes you
from a Maldivian breakfast to a private karaoke room, because it serves mashuni in the morning, burgers and
kottu all day, 70+ drinks and karaoke until 2 AM, and it's home of the 2 kg Bodugola.

== COLOURS ==
Web red #DD1638 (hero, drinks band, footer) · logo red #EA1D3C (logo only) · deep red #B80F2E (buttons,
headings on cream, prices; hover #9C0C26) · cream #FBEFE0 (page ground) · paper #FFF8EF (menu/signature
sections) · ink #22161A (text) · muted #6C5A5E · line #EBD6C6 · wine #5E1628 (visit section) · karaoke
violet #7B2FD0 (karaoke section only, gradient 135deg to wine). Never put small white text on #EA1D3C.
Single light brand theme (no dark mode).

== TYPOGRAPHY (Google Fonts) ==
Display: Playfair Display 900, UPPERCASE, line-height .86–.95, hero clamp(56px,11.5vw,150px),
H2 clamp(40px,6.4vw,76px). Accent: Playfair Display Italic 700 (tagline, review quotes).
Body: Titillium Web 400/600, 17px, line-height 1.55. Labels/buttons: Titillium Web 700 uppercase,
12–13px, letter-spacing .1–.12em.

== DESIGN LANGUAGE (reference: "Hanzo" restaurant template, adapted) ==
- Inset cream navbar (10px radius) floating 12px from the top over the red hero; fixed on scroll.
- Hero: centred pill badge with LIVE karaoke status (Maldives time UTC+5, open 10:00–02:00), H1 lines
  "LYRE IS" / "THE PLACE", then a row with "TO" on the left and "BE!" on the right, each with a small
  caps meta line ("BEACH ROAD" / "HULHUMALÉ") and a short rule. Between and below them sits a 16:9 video
  frame whose top is notched by those two red blocks. Thin cream line-doodles (burger, juice glass, mic,
  palm) float on the red.
- Video chapter bar across the bottom of the frame: "01 | 02 | 03 | 04" (seek to 0s, 3s, 5.6s, 9.6s),
  centre "BODUGOLA — The Giant Burger · 2 kg · MVR 500", a pause button, and a red "PRE-ORDER →" pill.
- Framed boards: 1.5px deep-red border + 1px inner rule at 7px inset + small lyre-instrument corner
  ornaments (22px squares). Cream sections carry a subtle wave-line pattern.
- Perforated "stamp" red card for reviews over a full-bleed food photo with round prev/next arrows.
- Photos: 4px radius; floating round plates rotated ±10° with soft shadow; arch-top frame for the drink video.
- Buttons: pills, min 46px tall. Motion: headline rise 0.9s, hover lifts, karaoke neon flicker; honour
  prefers-reduced-motion.

== PAGE STRUCTURE (single page with anchors; optional /menu route) ==
1 Navbar: logo (white Lyre mark in a red circle + "LYRE"), links Signatures · Menu · Karaoke · Visit,
  CTA "Book a room" → #karaoke. Mobile: "☰ Menu" full-screen red overlay + Call/WhatsApp buttons.
2 Hero (above). Video files: assets/video/bodugola-signature-landscape.mp4 (desktop),
  bodugola-signature-portrait.mp4 (≤760px), posters *-poster.jpg. Muted, loop, playsinline, autoplay
  unless reduced motion.
3 Intro: pill "CAFÉ · RESTAURANT · KARAOKE"; H2 "Maldivian mornings. Beachfront nights."; copy "A beachfront
  café on Hulhumalé's Beach Road. Mashuni and roshi for breakfast, burgers and kottu all day, and private
  karaoke rooms until 2 AM."; two floating round plates (nasi-goreng, mixed-grill); two photos with
  captions "Valhomas Mashuni MVR 80", "Kuda Gola burger MVR 125".
4 Signature plates (framed menu board, pill "LYRE PICKS"). List left, big showcase image right that swaps
  on hover/focus/tap with a caption overlay and a small inset photo:
  Bodugola, MVR 500: "a.k.a. The Giant Burger. A 2 kg beef burger with fries and salad. Pre-order only."
  Kuda Gola, MVR 125: "Beef burger with salad, fries and hot sauce."
  Lyre Special Nasi Goreng, MVR 120: "Fried rice with a fried egg, prawn, crackers and slaw."
  Chicken Cheese Kottu, MVR 110: "Kottu and chicken under a blanket of cheese sauce."
  Mix Mashuni, MVR 95: "Three types of mashuni with huni roshi or roshi."
  Button "See the full menu →".
5 Reviews stamp card: quote ONLY real, owner-approved reviews. Until approved use the public Tripadvisor
  review titles "Best burgers in town" and "This is where u can watch sunrise", attributed
  "Tripadvisor review title", plus [ADD OWNER-APPROVED GOOGLE REVIEWS].
6 "Sunrise to singalong": Morning, The Sunrise ("Mashuni, kulhimas and rihaakuru with warm roshi. Or French
  toast and pancakes.") · All day, Eat & sip ("Burgers, kottu, nasi goreng, pasta and grills, with 70+
  shakes, juices, mocktails and coffees.") · Till 2 AM, After dark ("Private karaoke rooms and the shisha
  lounge. Mixed Grill and Mix Kottu for the table.")
7 Karaoke (#karaoke): "Grab the mic." / "Private karaoke rooms for you and your crew, open 10 AM to 2 AM.
  Call or WhatsApp to book your slot." Info card: Open daily 10 AM – 2 AM; Rooms [CONFIRM NUMBER & CAPACITY];
  Rate [CONFIRM RATE]; Shisha available [CONFIRM FLAVOURS]; steps 1 Pick date/time/group size 2 Send on
  WhatsApp or call 949-9969 3 Lyre confirms. Buttons: WhatsApp pre-filled "Hi Lyre! I'd like to book a
  karaoke room on __ at __ for __ people." and Call.
8 Menu (#menu): sticky pill tabs. Show number, name, description, protein tags, "Lyre pick" tag, price.
  Note: "Prices in MVR, subject to 8% GST & 10% service charge." [CONFIRM MENU IS CURRENT] [CONFIRM PIZZA ITEMS]
  THE SUNRISE: 01 French Toast (egg of choice & sausage) 95 · 02 Pancakes (egg & sausage) 95 PICK ·
  03 Mix Mashuni (three types, huni roshi or roshi) 95 · 04 Kulhimas 80 · 05 Rihaakuru 80 · 06 Mashuni 75 ·
  07 Valhomas Mashuni 80 · 08 Fathu Mashuni 80 · 09 Baraboa (Pumpkin) Mashuni 80 (all with huni roshi or roshi)
  THIS & THAT: 10 Lyre Special Nasi Goreng 120 · 11 Meatball Spaghetti 125 · 12 Bamigoreng 120 ·
  13 Spaghetti Alfredo (seafood) 135 · 14 Meatball and Mash 120 · 15 Tuna Steak (sautéed vegetables) 125 ·
  16 Creamy Spaghetti (chicken) 105 · 17 Baked Spicy Rice (greens, chicken/beef) 120 PICK ·
  18 Honey Sesame Chicken (steamed rice) 105 PICK · 19 Kuda Gola (beef burger, salad, fries, hot sauce) 125 PICK ·
  20 The Rooster (chicken burger, salad, fries, hot sauce) 115 PICK · 21 Bodugola a.k.a. The Giant Burger
  (2 kg beef burger, fries & salad, pre-order) 500 PICK · 22 Madam Sandwich (chicken/beef/tuna) 90 PICK ·
  23 Chicken Chop 115 · 24 Chicken Sub 90 · 25 Beef Sub 110 · 26 Sandwich Chicken/Beef (salad, fries, hot
  sauce) 90 · 27 Mixed Grill (seafood, beef, chicken in black pepper sauce & garlic bread) 220 PICK ·
  28 Broccoli & Beef Stir Fry (steamed rice) 125
  KOTTU GANG: 29 Chicken Cheese Kottu 110 PICK · 30 Chicken Kottu 100 · 31 Beef Kottu 110 · 32 Mix Kottu 115
  SMALL & LIGHT: 33 Green Salad (chicken on request) 100 · 34 Beef & Fries 95 · 35 Cheese & Fries 95 ·
  36 Caesar Salad (romaine, croutons, parmesan, Caesar dressing) 120 PICK · 37 Onion Rings 50
  THE LAST MEAL: 38 Nutella Sandwich 100 PICK · 39 Fresh Fruits (seasonal) 100 · 40 Ice Cream Scoop
  (chocolate, vanilla, strawberry) 60
  DRINKS: Thick Shakers: Strawberry/Chocolate/Vanilla Milkshake 79, Banana/Mango Milkshake 79, Oreo Milkshake
  89, Ice Milo 89, Ice Coffee 89, Mixed Berry Blast 89, Oatmeal with Papaya 69, Single/Double Creamy Espresso
  33/67. Mocktails: Mint & Lime 69, Passionfruit & Turmeric 69, Mango Mania 89, Strawberry Margarita 69, Lady
  Blue 79, Watermelon Breeze 79, Pomegranate Bull 79, Redbull Rooster 89, Kanbulo 89, Aloha 79, Blueberry
  Mojito 59, Ginger Lemonade 69. Fresh Chilled: Orange & Pineapple 69, Watermelon & Orange 59, Passionfruit &
  Pineapple 69, Beetroot 69, Orange 59, Watermelon 59, Pineapple 59, Passionfruit 69, Lime 39, Carrot 59,
  Mixed Fruit 79. Hot Stuff: Espresso 39, Americano 49, Cappuccino 59, Café Mocha 69, Hot Chocolate 69,
  Hazelnut Latte 69, Milk Tea 29, Hot Milo 74, Assorted Tea 19, Teh Trik 33. Others: Soda Gembira 45, Ice
  Lemon Tea 45, Granini 31, Iced Milk 34, Water 10/15, Nuts 14, Coke/Zero/Sprite/Soda 19, Bitter Lemon 22,
  Red Bull 59, Beer 0% 59.  SHISHA: [CONFIRM FLAVOURS & PRICES]
9 Drinks band (red): "Vibrant layers, bold taste." / "Thick shakes, fresh juices and house mocktails.
  Seventy-plus ways to cool down on Beach Road." Chips with 7 drinks + prices. Lyre's own carrot-juice reel
  (assets/video/carrot-juice-reel.mp4, arch frame, plays only when on screen) + spaghetti photo.
10 "On the feed": 6 real photos linking to Instagram; button "Follow @lyre.mv".
11 Visit (#visit, wine background): paper card with "Find us on Beach Road", address, big selectable phone
  949-9969 + Copy button, hours table (Café & kitchen [CONFIRM OPENING HOURS]; Karaoke 10 AM – 2 AM; Seating
  Outdoor · Dine-in; Payment [CONFIRM PAYMENT METHODS]), buttons Get directions (Google Maps search
  "Lyre Cafe Beach Road Hulhumale") + WhatsApp, FAQ (tax: "No. Menu prices are subject to 8% GST and 10%
  service charge." · Bodugola: "Pre-order only. Call or WhatsApp 949-9969. Notice time: [CONFIRM]" ·
  Table booking [CONFIRM] · Delivery [CONFIRM]). Illustrated map card linking to Google Maps. Do not embed
  a Google Maps iframe until the exact pin is confirmed [CONFIRM MAP PIN].
12 Footer (red): white logo, italic "is the place to be!", Visit list, Follow list.
13 Sticky mobile bottom bar (≤760px): Call (red) · WhatsApp · Menu · Directions, safe-area aware.

== IMAGES ==
Use ONLY the restaurant's real photos in assets/img (bodugola-web, kuda-gola, nasi-goreng,
chicken-cheese-kottu, mix-mashuni, valhomas-breakfast, honey-sesame-chicken, mixed-grill, french-toast,
spaghetti-broccoli, carrot-juice, carrot-juice-tray, beach-salad, pizza-campaign, logo-white.png).
Never generate AI food photos. Placeholders: [UPLOAD HIGH-RESOLUTION LOGO], [UPLOAD KARAOKE ROOM PHOTO],
[UPLOAD EXTERIOR PHOTO], [UPLOAD INTERIOR PHOTO]. Alt text pattern: "[Dish] at Lyre, Hulhumalé".

== UX / MOBILE ==
Mobile-first. 16px side gutter. Tap targets ≥44px. Menu tabs horizontally scrollable and sticky under
the nav; remember last tab (localStorage, fail-safe). Overlay nav closes on Esc and link tap. Phone number is
always visible as text (links may not work in every context). Footer bottom padding clears the sticky bar.

== SEO ==
<title>Lyre Restaurant & Café · Beach Road, Hulhumalé</title>
Meta description: "Lyre Restaurant & Café on Beach Road, Hulhumalé. Beachfront burgers, Maldivian breakfast,
kottu, 70+ drinks and private karaoke rooms 10 AM – 2 AM. Call 949-9969."
H1: "Lyre is the place to be!". JSON-LD Restaurant schema (name, alternateName, address, telephone,
servesCuisine, priceRange "MVR 50–500", sameAs, amenityFeature) + openingHours [CONFIRM] + Menu schema.
OG image = hero video poster. Keywords: Lyre Hulhumalé, burger Hulhumalé, karaoke Hulhumalé, Maldivian
breakfast Hulhumalé, beachfront café Hulhumalé, Bodugola.

== ACCESSIBILITY & PERFORMANCE ==
WCAG 2.2 AA (use the contrast pairs above), visible focus rings, aria labels on icon buttons,
aria-current on video chapters, video pause button, prefers-reduced-motion disables autoplay/animations.
WebP images with width/height, lazy loading below the fold, fonts display=swap, MP4 +faststart.
Targets: LCP < 2.5s on 4G, CLS < 0.1. Track clicks on tel:, wa.me, Maps and menu tabs.

== FUNCTIONAL ==
Live karaoke status in UTC+5. Video chapter seek + active state. Signature board image swap. Review
prev/next. Copy-phone button with clipboard fallback. WhatsApp links with pre-filled text. No backend forms.

== DO NOT ==
Invent reviews, ratings, awards, halal status, delivery, founding year, opening hours, prices not
listed above, or any claim marked [CONFIRM]. Do not show accounts@vtravelsmaldives.com.
```

---

## 36. Prototype Priority

| MUST HAVE (in prototype ✅) | SHOULD HAVE | NICE TO HAVE | DO NOT BUILD YET |
|---|---|---|---|
| Hero + Bodugola video ✅ | Real café opening hours & schema | Karaoke availability calendar | Online ordering / cart |
| Signature board ✅ | Separate `/menu` page | Dhivehi language version | Table-booking software |
| Full menu with prices ✅ | Approved Google reviews | Instagram API feed | Loyalty / accounts |
| Karaoke booking via WhatsApp ✅ | Real exterior/interior/karaoke photos | Bodugola "challenge" wall | Delivery integration |
| Visit: address, phone, map, FAQ ✅ | Vector logo; favicon set | Seasonal promos banner | Blog |
| Sticky mobile bar ✅ | Analytics events | Re-shot 4K Bodugola film | Multi-branch structure |
| Schema & meta ✅ | Google Business Profile clean-up | | |

---

## 37. Final Verification Checklist

| # | Question | Answer |
|---|---|---|
| 1 | Does the website reflect this restaurant? | ✅ Uses Lyre's own photos, reel, tagline, menu names and red identity |
| 2 | Palette from existing identity? | ✅ Red measured from the logo (#EA1D3C); deeper tones from Lyre's studio shots and Linktree gradient; violet from the karaoke graphic |
| 3 | Recommended products actually sold? | ✅ All on the supplied menu. ⚠️ Pizza is promoted but not on the menu, so it's shown only as a campaign image |
| 4 | USPs evidence-based? | ✅ §9 split verified / inferred / forbidden |
| 5 | Audience supported? | 🟡 Inferred from services & reviews; confirm |
| 6 | Business details verified? | 🟢 phone, address, karaoke hours · 🔴 café hours, WhatsApp, payment, delivery |
| 7 | Old posts mistaken for current? | ⚠️ "White Harp" references and Tripadvisor data are older; not used as current facts. The Jan 2024 @lyre.mvone01 post is flagged |
| 8 | Competitor observations accurate? | 🟡 From listings/snippets only |
| 9 | Invented claims? | None. Reviews are real public titles, labelled as such; all gaps tagged `confirm` |
| 10 | Missing assets? | Vector logo, interior/exterior, karaoke room, hours, rates |
| 11 | Structure fits the business? | ✅ Call/WhatsApp-led single page; no e-commerce |
| 12 | Mobile considered? | ✅ Portrait hero video, sticky bar, overlay nav, scrollable tabs |
| 13 | Buildable without guessing? | ✅ §35 master prompt + prototype source |
| 14 | Convincing for the owner? | ✅ Prototype + signature video from their own photo |

**Address discrepancy (flagged):** Facebook About says "Café Lyre, kaani magu (Beach Road), Male, Maldives, 23000"; the 9 Sep post says "Maldives, Hulhumale', Lot 11075, Beach Road". Hulhumalé is part of Malé City and Kaani Magu is Beach Road, so the two probably describe the same place 🟡. The website uses the more specific **Lot 11075, Beach Road, Hulhumalé**. Ask the owner to update Facebook About to match.

---

## 38. Sources

**Supplied by client (primary)**
- Facebook About screenshot: address, links, services, phone, email, photo grid
- Facebook post, 9 Sep: "Fresh, cheesy, and impossible to resist", Lot 11075 address, phone, #lyremv
- Instagram screenshot: @lyre.mvone01 post, 1 Jan 2024, Spaghetti & Broccoli
- Linktree screenshot: "Lyre Restaurant & Café", *New* Karaoke Rooms 10AM–02AM, Menu (Google Drive)
- WhatsApp video: Lyre carrot-juice reel with "Lyre is the place to be!" end card
- Company data: `lyre-website-prototype.html` (menu, prices, photos)
- Design reference: "Hanzo" restaurant template screenshot
- X reference (not accessible in this session): https://x.com/KrevixAi/status/2089970183674663188

**Web (search results; pages themselves blocked)**
- [Tripadvisor: LYRE, Hulhumale](https://www.tripadvisor.com/Restaurant_Review-g1938013-d10109309-Reviews-Lyre-Hulhumale.html)
- [Tripadvisor review: "Best burgers in town"](https://www.tripadvisor.com/ShowUserReviews-g1938013-d10109309-r375205408-Lyre-Hulhumale.html)
- [Tripadvisor review: "This is where u can watch sunrise"](https://www.tripadvisor.com/ShowUserReviews-g1938013-d10109309-r820269597-Lyre-Hulhumale.html)
- [Tripadvisor photo: "Cafe' Lyre – White Harp Beach"](https://tripadvisor.com/LocationPhotoDirectLink-g1938013-d9598781-i166420891-White_Harp_Beach_Maldives-Hulhumale.html)
- [Tripadvisor photo: "Tuna Kottu – Lyre"](https://www.tripadvisor.com/LocationPhotoDirectLink-g1938013-d10109309-i367982685-Lyre-Hulhumale.html)
- [Mindtrip: Lyre Restaurant & Karaoke](https://mindtrip.ai/restaurant/hulhumale-maldives/lyre-restaurant-karaoke/re-C9OmYesS)
- [Facebook: Lyre (CafeLyre)](https://www.facebook.com/CafeLyre/)
- [Instagram: Lyre Cafe with Karaoke Lounge (@lyre.mv)](https://www.instagram.com/lyre.mv/)
- [Linktree: Lyre.mv](https://linktr.ee/Lyre.mv)
- [The White Harp Inn](https://whiteharpbeach.com/)
- [Tripadvisor: Best cafés in Hulhumale](https://www.tripadvisor.com/Restaurants-g1938013-c8-Hulhumale.html)
- [Wanderlog: best restaurants in Hulhumale](https://wanderlog.com/list/geoCategory/198552/where-to-eat-best-restaurants-in-hulhumale)
- [My Maldives Guide: Hulhumalé restaurants](https://mymaldivesguide.com/hulhumale-restaurants/)
- [Evendo: best restaurants in Hulhumalé](https://evendo.com/locations/maldives/hulhumale/best-restaurants)
- [Evendo: Rivo Lounge and Karaoke](https://evendo.com/locations/maldives/hulhumale/landmark/rivo-lounge-and-karaoke)
- [Evendo: Dinemore Hulhumalé](https://evendo.com/locations/maldives/hulhumale/restaurant/dinemore-hulhumale)
- [Instagram: Rivo (@rivo.mv)](https://www.instagram.com/rivo.mv/)
