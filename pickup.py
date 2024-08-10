import streamlit as st

# Define pickup lines
pickup_lines = {
    'boy': {
        'love': [
            "Do you have a name, or can I call you mine?",
            "Are you a magician? Because whenever I look at you, everyone else disappears.",
            "Do you have a map? Because I keep getting lost in your eyes.",
            "Is your name Google? Because you have everything I’ve been searching for.",
            "If you were a vegetable, you’d be a cute-cumber."
        ],
        'fun': [
            "Are you a campfire? Because you’re hot and I want s’more.",
            "Do you believe in love at first sight, or should I walk by again?",
            "If you were a fruit, you’d be a fineapple.",
            "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
            "I must be a snowflake, because I’ve fallen for you."
        ]
    },
    'girl': {
        'love': [
            "Are you a magician? Because whenever I look at you, everyone else disappears.",
            "If you were a vegetable, you’d be a cute-cumber.",
            "Do you have a map? Because I keep getting lost in your eyes.",
            "Is your name Google? Because you have everything I’ve been searching for.",
            "Do you have a name, or can I call you mine?"
        ],
        'fun': [
            "Do you believe in love at first sight, or should I walk by again?",
            "If you were a fruit, you’d be a fineapple.",
            "Are you a campfire? Because you’re hot and I want s’more.",
            "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
            "I must be a snowflake, because I’ve fallen for you."
        ]
    }
}

# Streamlit UI
st.title('Pickup Line Generator')

# Input fields
keyword = st.text_input('Enter a keyword for the pickup line (e.g., love, fun):')
gender = st.radio('Who do you want the pickup line for?', ['boy', 'girl'])

if keyword and gender:
    # Normalize keyword
    keyword = keyword.lower().strip()

    # Determine pickup line category
    line_category = 'love' if 'love' in keyword else 'fun'

    # Filter pickup lines based on gender and keyword
    lines = pickup_lines.get(gender, {}).get(line_category, [])

    # Display a random pickup line
    if lines:
        import random
        selected_line = random.choice(lines)
        st.subheader('Here\'s a pickup line for you:')
        st.write(selected_line)
    else:
        st.write('No pickup lines found for the given input. Try a different keyword.')
