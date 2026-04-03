
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("waste_classifier_final.keras", compile = False)
    return model

model = load_model()

# Class names (10 classes)
CLASS_NAMES = ['battery', 'organics', 'cardboard', 'clothes','glass', 'metal', 'paper', 'plastic', 'shoes', 'trash']

AWARENESS = {
    "cardboard":{
        "type":"♻️ Recyclable, Reusable & Compostable",
        "info":(
            "**Cardboard** is highly recyclable, biodegradable, and reusable. "
        "It's made from paper fibers and can be recycled up to 7 times before the fibers weaken. "
        "Cardboard production consumes significant water and energy, contributing to deforestation when not sourced sustainably. "
        "Recycling cardboard reduces landfill waste, saves trees, and cuts greenhouse gas emissions by 30%. "
        "\n\n"
        ),
        "Environmental Impact":(
            "Recent studies show that recycling one ton of cardboard saves 17 trees and 7,000 gallons of water. "
        "However, contaminated cardboard (with food waste or grease) cannot be recycled and ends up in landfills where it releases methane. "
        "In 2025, experts emphasize reducing single-use packaging and reusing boxes multiple times before recycling to maximize environmental benefits."
        "\n\n"
        ),
        "local_action": (
            "**🛠️ DIY Treatment & Reuse Ideas:**\n\n"
            "**Composting Method:**\n\n"
            "\t• Tear cardboard into 2-inch pieces, remove tape/staples\n\n"
            "\t• Soak in water for 24 hours to soften\n\n"
            "\t• Mix with kitchen scraps (3 parts cardboard : 1 part food waste)\n\n"
            "\t• Keep pile moist and turn weekly\n\n"
            "\t• Ready in 2-3 months as nutrient-rich compost for garden\n\n"
            "**Creative Reuse Projects:**\n\n"
            "\t• Build storage organizers, drawer dividers, desk caddies\n\n"
            "\t• Create cat scratching posts or pet houses\n\n"
            "\t• Make DIY planters (line with plastic, fill with soil)\n\n"
            "\t• Craft kids' toys: playhouses, robot costumes, puppet theaters\n\n"
            "\t• Use as garden mulch or weed barrier (lay flat around plants)\n\n"
            "\t• Cut into stencils for art projects or spray painting\n\n"
            "\t• Shred for eco-friendly packing material"
        )
    },
    "glass":{
        "type":"🌿 100% Recyclable & Infinitely Reusable",
        "info" : (
             "**Glass** is 100% recyclable, reusable, and can be recycled endlessly without quality loss. "
        "Unlike plastic, glass doesn't release harmful chemicals and remains inert in the environment. "
        "However, when not recycled, glass persists in landfills for thousands of years, taking up valuable space. "
        "Recycling glass saves 30% energy compared to producing new glass from raw materials and reduces mining needs. "
        "\n\n"
        ),
        "Environmental Impact":(
            "According to 2025 data, recycling glass reduces carbon emissions equivalent to removing 0.19 million cars annually. "
        "The challenge is that glass is heavy and costly to transport, making collection programs less efficient in some regions. "
        "New crushing technologies and improved sorting systems are being implemented globally to boost glass recycling rates and reduce environmental footprint."
        "\n\n"
        ),
        "local_action": (
            "**🛠️ DIY Treatment & Reuse Ideas:**\n\n"
            "**Direct Reuse Projects:**\n\n"
            "\t• Transform jars into food storage containers (spices, dry goods, leftovers)\n\n"
            "\t• Create terrariums: layer pebbles, charcoal, soil, and small plants\n\n"
            "\t• Make candle holders (add sand and tea lights)\n\n"
            "\t• Build herb gardens (punch drainage holes, add soil)\n\n"
            "\t• Design vases and flower arrangements\n\n"
            "\t• Organize bathroom supplies (cotton balls, Q-tips, bath salts)\n\n"
            "\t• String LED fairy lights inside for ambient lighting\n\n"
            "\t• Layer cookie/brownie ingredients for unique gift packaging\n\n"
            "**Advanced DIY:**\n\n"
            "\t• Cut bottles with string-and-fire method to make drinking glasses\n\n"
            "\t• Create mosaic art from broken glass pieces\n\n"
            "\t• Make photo display jars with decorative fillers"
        )
    },
    "metal" : {
        "type" : "⚙️ Recyclable & Infinitely Reusable",
        "info" : (
            "**Metal** waste (aluminum, steel, copper) is 100% recyclable and can be reused indefinitely without degradation. "
        "Recycling metal requires 95% less energy than mining new ore and prevents toxic heavy metal contamination in soil and water. "
        "Despite its recyclability, improper disposal leads to environmental damage from mining waste and industrial pollution. "
        "Metal recycling reduces greenhouse gas emissions by millions of metric tons annually. "
        "\n\n"
        ),
        "Environmental Impact":(
            "EPA data from 2025 shows recycling metals prevents 29.16 million metric tons of CO2 emissions yearly, equivalent to taking 6.3 million cars off the road. "
        "However, recent studies warn that mining waste continues releasing dangerous pollutants into rivers in developing countries. "
        "Expanding metal collection programs and improving recycling infrastructure are critical to reducing industrial pollution and resource depletion."
        "\n\n"
        ),
        "local_action": (
            "**🛠️ DIY Treatment & Reuse Ideas:**\n\n"
            "**Preparation for Recycling:**\n\n"
            "\t• Rinse thoroughly to remove food residue\n\n"
            "\t• Remove labels and plastic coatings\n\n"
            "\t• Flatten aluminum cans to save space\n\n"
            "\t• Separate steel (magnetic) from aluminum (use magnet test)\n\n"
            "\t• Collect 5-10kg and sell to scrap dealers for extra income\n\n"
            "**Creative Upcycling:**\n\n"
            "\t• Convert tins into planters (punch drainage holes, paint exterior)\n\n"
            "\t• Make desk organizers for pens, scissors, brushes\n\n"
            "\t• Create DIY lanterns (punch decorative patterns, add candles)\n\n"
            "\t• Build vertical hanging gardens on wooden boards\n\n"
            "\t• Design bird feeders (cut openings, fill with seeds)\n\n"
            "\t• Organize workshop tools (nails, screws, washers)\n\n"
            "\t• Craft kids' musical instruments (decorate as drums)"
        )
    },
    "paper":{
        "type":"📄 Recyclable, Reusable & Compostable",
        "info" : (
            "**Paper** is recyclable and can be composted or reused for packaging and crafts. "
        "It can be recycled 5-7 times before fibers break down, making it a sustainable material when managed properly. "
        "However, paper production drives deforestation (35% of harvested trees go to paper), consumes massive water resources, and releases toxic dioxins during bleaching. "
        "Recycling paper saves trees, reduces landfill waste, and cuts energy use by 60%. "
        "\n\n"
        ),
        "Environmental Impact":(
            "In 2025, recycling paper prevented 155.17 million metric tons of CO2 emissions, equal to removing 33.52 million cars from roads. "
        "Despite this, the U.S. alone discards 16 billion paper cups annually, and paper mill wastewater harms aquatic ecosystems with neurotoxins and carcinogens. "
        "Switching to digital alternatives, using recycled paper, and reducing single-use paper products can drastically lower environmental impact."
        "\n\n"
        ),
        "local_action": (
            "**🛠️ DIY Treatment & Reuse Ideas:**\n\n"
            "**Composting Method:**\n\n"
            "\t• Shred paper into strips\n\n"
            "\t• Mix with kitchen waste (1:1 ratio)\n\n"
            "\t• Keep moist and turn weekly\n\n"
            "\t• Decomposes in 4-6 weeks into garden compost\n\n"
            "**DIY Handmade Paper:**\n\n"
            "1. Tear paper into small pieces, soak overnight\n\n"
            "2. Blend with water into pulp\n\n"
            "3. Pour onto fine mesh screen, spread evenly\n\n"
            "4. Press out water with sponge\n\n"
            "5. Let dry flat for 24 hours\n\n"
            "6. Use for greeting cards, gift tags, art projects\n\n"
            "**Creative Reuse:**\n\n"
            "\t• Make fire starters (roll tightly, tie with twine, dip ends in wax)\n\n"
            "\t• Create papier-mâché crafts (bowls, masks, sculptures)\n\n"
            "\t• Craft paper beads for jewelry (roll thin strips, seal with glue)\n\n"
            "\t• Use as garden mulch (wet layers prevent weeds)\n\n"
            "\t• Make seed paper (add wildflower seeds to pulp, dry, plant)\n\n"
            "\t• Reuse as wrapping paper or packing material"
        )
    },
    "plastic":{
        "type": "🚯 Limited Recyclability (Only 9% gets recycled globally)",
        "info": (
            "**Plastic** is technically recyclable but difficult to manage—most types degrade during recycling and only 9% gets recycled globally. "
        "It is non-biodegradable, taking 200-500 years to decompose, and breaks into harmful microplastics that pollute oceans, soil, and even our food. "
        "Plastic production consumes 20% of global oil and gas supplies and contributes over 3% of global greenhouse gas emissions. "
        "Burning or dumping plastic releases toxic chemicals harmful to wildlife and human health. "
        "\n\n"
        ),
        "Environmental Impact":(
            "In 2025, scientists confirmed microplastics are present in 80% of tap water worldwide and nanoplastics can transport heavy metals like lead and cadmium, intensifying toxicity. "
        "The Great Pacific Garbage Patch is now three times the size of France. "
        "Countries are implementing single-use plastic bans and producer responsibility laws to combat the crisis. Opt for reusable alternatives and always recycle properly."
        "\n\n"
        ),
        "local_action": (
            "**🛠️ DIY Treatment & Reuse Ideas:**\n\n"
            "**⚠️ NEVER BURN PLASTIC (releases toxic fumes)**\n\n"
            "**Eco-Brick Method (Soft Plastics):**\n\n"
            "\t• Clean and dry all plastic wrappers/bags\n\n"
            "\t• Stuff tightly into empty plastic bottles using stick\n\n"
            "\t• Pack until bottle is rock-hard (no air gaps)\n\n"
            "\t• Use for building furniture, garden beds, or donate to construction projects\n\n"
            "**Plastic Bottle Upcycling:**\n\n"
            "\t• Cut horizontally for vertical garden planters\n\n"
            "\t• Create bird feeders (cut openings, add perches)\n\n"
            "\t• Make funnels and scoops (cut diagonally)\n\n"
            "\t• Build drip irrigation (poke holes, bury near plants)\n\n"
            "\t• Design desk organizers or cosmetic holders\n\n"
            "**Plastic Container Reuse:**\n\n"
            "\t• Store craft supplies, screws, buttons\n\n"
            "\t• Use as seedling pots (punch drainage holes)\n\n"
            "\t• Repurpose as lunch containers\n\n"
            "**Plastic Bag Crafts:**\n\n"
            "\t• Weave into durable mats or baskets (YouTube tutorials)\n\n"
            "\t• Reuse as trash bin liners\n\n"
            "\t• Crochet into tote bags or storage containers"
        )
    },
    "trash":{
        "type":"🗑️ Non-Recyclable, Non-Reusable (Landfill or Incineration)",
        "info": (
            "**Trash** (mixed or non-recyclable waste) is typically non-recyclable, non-reusable, and ends up in landfills or incinerators. "
        "Landfilled trash releases methane—a greenhouse gas 28 times more potent than CO2—and contaminates soil and groundwater. "
        "Over 2 billion metric tons of waste are generated globally each year, with only 19% recycled and 30% going to controlled landfills. "
        "Reducing single-use products, composting organic waste, and proper disposal are critical to minimizing environmental harm. "
        "\n\n"
        ),
        "Environmental Impact":(
            "Recent reports reveal that landfills have recorded over 1,000 major methane leaks since 2019, accelerating climate change. "
        "American waste exports are causing 'hidden tsunamis' of pollution in Southeast Asia, where improper disposal harms air and water quality. "
        "By 2050, global waste is projected to reach 3.8 billion metric tons. Urgent action—reducing consumption, improving waste separation, and supporting circular economy initiatives—is essential to prevent environmental collapse."
        "\n\n"
        ),
        "local_action": (
            "**🛠️ DIY Waste Management at Home:**\n\n"
            "**Composting Organic Waste (Kitchen Scraps):**\n\n"
            "**Method 1: Backyard Composting**\n\n"
            "\t• Layer greens (food scraps) with browns (leaves, paper) 1:3 ratio\n\n"
            "\t• Keep pile moist like a squeezed sponge\n\n"
            "\t• Turn every 2 weeks with shovel\n\n"
            "\t• Ready in 2-3 months as rich soil\n\n"
            "**Method 2: Bokashi Composting (Apartments)**\n\n"
            "\t• Use sealed bucket with Bokashi bran\n\n"
            "\t• Add daily food scraps (even meat/dairy)\n\n"
            "\t• Ferments in 2 weeks, then bury in soil\n\n"
            "\t• No outdoor space needed\n\n"
            "**Method 3: Vermicomposting (Worm Bin)**\n\n"
            "\t• Buy/build worm bin with red wigglers\n\n"
            "\t• Feed kitchen scraps weekly\n\n"
            "\t• Harvest compost every 3-4 months\n\n"
            "\t• Odorless when maintained properly\n\n"
            "**Method 4: Trench Composting**\n\n"
            "\t• Dig 8-12 inch trench in garden\n\n"
            "\t• Bury food scraps directly\n\n"
            "\t• Cover with soil, decomposes naturally\n\n"
            "**Repair & Repurpose:**\n\n"
            "\t• Fix torn clothes, broken electronics, furniture\n\n"
            "\t• Turn old t-shirts into cleaning rags\n\n"
            "\t• Convert worn jeans into tote bags or coasters\n\n"
            "\t• Donate functional items to charity or community groups"
        )
    },
    "organics":{
        "type":"🌱 Compostable & Biodegradable Organic Waste",
        "info": (
            "**Organic waste** (food scraps, yard waste, natural fibers) is biodegradable and can be composted into nutrient-rich soil. "
            "Composting diverts waste from landfills and reduces methane emissions by up to 50%. When properly managed, organic waste becomes a valuable resource for gardens and agriculture. "
            "Food waste alone represents 8-10% of global greenhouse gas emissions when decomposed in landfills. "
        ),
        "Environmental Impact":(
            "Composting 1 ton of organic waste prevents 1.5 tons of CO2-equivalent emissions from entering the atmosphere. "
            "Industrial composting facilities process millions of tons annually, returning nutrients to soil ecosystems. "
            "However, improper disposal in landfills creates anaerobic conditions that produce methane, a potent greenhouse gas. "
        ),
        "local_action": (
            "**🛠️ DIY Composting Methods:**\n\n"
            "**Home Composting:**\n"
            "\t• Use a bin or pile in your garden\n"
            "\t• Layer green waste (food/grass) with brown waste (leaves/paper)\n"
            "\t• Keep moist and turn regularly\n"
            "\t• Ready in 2-3 months\n\n"
            "**Vermicomposting (Worm Composting):**\n"
            "\t• Use red wiggler worms in a bin\n"
            "\t• Add food scraps weekly\n"
            "\t• No smell or outdoor space needed\n"
            "\t• Harvest nutrient-rich compost every 3-4 months"
        )
    },
    "wood":{
        "type":"🌳 Recyclable & Reusable Wood Waste",
        "info": (
            "**Wood waste** from construction, furniture, and packaging can be recycled, repurposed, or composted. "
            "Recycled wood reduces demand for virgin timber, preserving forests and their carbon-sequesting capacity. "
            "Untreated wood can be composted or used as mulch, while pressure-treated or painted wood requires special handling to prevent toxic chemical release. "
        ),
        "Environmental Impact":(
            "Recycling wood waste prevents deforestation and saves millions of trees annually. "
            "Wood processing and disposal in landfills releases methane as the material decomposes. "
            "Reusing wood through furniture restoration or construction reduces the need for new lumber, lowering carbon emissions and forest destruction. "
        ),
        "local_action": (
            "**🛠️ Wood Waste Management:**\n\n"
            "**Reuse & Upcycling:**\n"
            "\t• Convert pallets into furniture, planters, or garden beds\n"
            "\t• Use scrap wood for DIY home projects\n"
            "\t• Donate wood to community workshops\n\n"
            "**Recycling & Composting:**\n"
            "\t• Chop untreated wood into mulch for gardens\n"
            "\t• Take pressure-treated wood to hazardous waste facilities\n"
            "\t• Compost untreated sawdust and wood chips"
        )
    },
    "shoes":{
        "type":"👟 Reusable & Recyclable Shoe Waste",
        "info": (
            "**Shoe waste** (footwear, textile materials) can be reused, donated, or recycled. "
            "The fast fashion industry generates 92 million tons of textile waste annually from clothing and footwear. Most shoes end up in landfills where they take 200+ years to decompose. "
            "Recycling and reusing shoes reduces water pollution from dye production and saves energy compared to manufacturing new footwear. "
        ),
        "Environmental Impact":(
            "Producing one pair of shoes requires significant water and generates pesticide pollution from material production. "
            "Shoe manufacturing and textile dyeing are among the largest polluters of water globally, responsible for 20% of industrial water pollution. "
            "Extending shoe life through maintenance and repair can reduce environmental impact by 20-30% compared to new production. "
        ),
        "local_action": (
            "**🛠️ Shoe Waste Solutions:**\n\n"
            "**Repair & Reuse:**\n"
            "\t• Repair soles and heels at professional cobblers\n"
            "\t• Fix small tears and loose seams\n"
            "\t• Donate wearable shoes to charities\n\n"
            "**Creative Upcycling:**\n"
            "\t• Use old shoes as planters (fill with soil)\n"
            "\t• Create shoe organizers for storage\n"
            "\t• Transform into wall decor or garden decorations\n"
            "\t• Make dog toys or pet beds from cushioning\n\n"
            "**Recycling:**\n"
            "\t• Take worn shoes to shoe recycling centers\n"
            "\t• Donate to secondhand stores\n"
            "\t• Use with textile recycling programs"
        )
    },
    "clothes":{
        "type":"👕 Reusable & Recyclable Clothing Waste",
        "info": (
            "**Clothing waste** (garments, fabrics, textiles) can be reused, donated, or recycled. "
            "The fast fashion industry generates 92 million tons of textile waste annually. Most clothes end up in landfills where they take 200+ years to decompose. "
            "Recycling and reusing clothes reduces water pollution from dye production and saves energy compared to manufacturing new fabrics. "
        ),
        "Environmental Impact":(
            "Producing one cotton t-shirt requires 2,700 liters of water and generates significant pesticide pollution. "
            "Textile dyeing is the second-largest polluter of water globally, responsible for 20% of industrial water pollution. "
            "Extending garment life through repair and reuse can reduce environmental impact by 20-30% compared to new production. "
        ),
        "local_action": (
            "**🛠️ Clothing Waste Solutions:**\n\n"
            "**Repair & Reuse:**\n"
            "\t• Mend holes, tears, and loose seams\n"
            "\t• Alter clothing to fit better\n"
            "\t• Donate wearable items to charities\n\n"
            "**Creative Upcycling:**\n"
            "\t• Cut old shirts into cleaning rags\n"
            "\t• Weave textiles into rugs or wall hangings\n"
            "\t• Transform jeans into bags or shorts\n"
            "\t• Make tote bags from old fabrics\n\n"
            "**Recycling:**\n"
            "\t• Take worn clothing to textile recycling centers\n"
            "\t• Donate to secondhand clothing stores"
        )
    },
    "battery":{
        "type":"⚠️ Hazardous Waste - Special Handling Required",
        "info": (
            "**Hazardous waste** (batteries, electronics, chemicals, paint, light bulbs) contains toxic materials that contaminate soil and groundwater when improperly disposed. "
            "Hazardous waste requires specialized collection and processing to prevent environmental and health damage. "
            "Many hazardous materials can be safely recovered and recycled through certified facilities. "
        ),
        "Environmental Impact":(
            "Improper disposal of hazardous waste causes soil and water contamination affecting millions. "
            "Electronic waste contains rare earth elements and toxic metals (lead, mercury, cadmium) that poison ecosystems for decades. "
            "Recycling hazardous materials recovers valuable resources while preventing toxic pollution. "
        ),
        "local_action": (
            "**🛠️ Hazardous Waste Disposal:**\n\n"
            "**DO NOT throw in regular trash:**\n"
            "\t• Batteries (alkaline, rechargeable, car batteries)\n"
            "\t• Electronics (phones, computers, TVs, appliances)\n"
            "\t• Paint, solvents, pesticides, motor oil\n"
            "\t• Light bulbs (fluorescent, LED, halogen)\n"
            "\t• Medical waste (needles, medications)\n\n"
            "**Safe Disposal Methods:**\n"
            "\t• Take to hazardous waste collection events\n"
            "\t• Visit local waste management centers\n"
            "\t• Use manufacturer take-back programs (electronics)\n"
            "\t• Contact professional disposal services\n"
            "\t• Never burn or bury hazardous materials"
        )
    }

}


# Streamlit app UI
st.title("♻️ Waste Classification & Awareness App")
st.write("Upload an image of waste to classify it and learn its environmental impact.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess image
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    predictions = model.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0]) * 100

    # Show results
    st.success(f"Predicted Class: **{predicted_class.capitalize()}**")
    st.write(f"Confidence: {confidence:.2f}%")

    # Show environmental awareness message
    # st.info(AWARENESS[predicted_class])

    # Get the awareness info for the predicted class
    info = AWARENESS[predicted_class]

    # Display the waste type
    st.write(f"### {info['type']}")

    # Show environmental impact
    st.write("#### Information")
    st.info(info['info'])

    # Show recent news
    st.write("#### Environmental Impact")
    st.warning(info['Environmental Impact'])

    # Show DIY actions (most important - expanded by default)
    st.write("#### What You Can Do Locally")
    st.success(info['local_action'])

st.write("---")










