from openai import OpenAI
import os 

client = OpenAI()
api_key = os.environ.get('OPENAI_API_KEY')

text = """
CONTENTS: The image depicts a serene seascape scene at sunset. A person is sitting at the stern of a small sailboat, which is the focal point in the foreground. The background features a calm harbor with more sailboats moored and a rocky pier extending into the water. A vivid sunset is displayed in the sky, and its reflection dances on the water's surface.
TECHNIQUE: The artwork utilizes a digital painting technique with clear, confident brush strokes that suggest movement, particularly in the water. It is done in a semi-stylized manner, blending realism with graphic elements. The brushwork in the sky and water suggests a dynamic texture, emphasizing the reflective and transient nature of light.
COLORS: The color palette is vibrant with a dominant use of warm tones like orange, red, and yellow for the sky and their reflections in the water, contrasting against the cooler blues and teals of the sea. The sun, as a bright yellow-white disc, stands out against the warmer hues of the sky, giving a harmonious balance between warm and cool colors.
"""

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are an art expert and amazing writer."},
        {"role": "user", "content": f"rewrite following text exactly, highlighting in UPPERCASE the most significant keywords to describe the opera, then assign a title (5/7 words) to the opera :\n\n{text}"}
    ]
)
print(response.choices[0].message.content)
