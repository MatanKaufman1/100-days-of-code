# 🎨 Hirst Painting

This project generates a **Hirst-style dot painting** using Python's `turtle` module. The colors are extracted from an image using the `colorgram` library and then used to create a randomized dot pattern inspired by **Damien Hirst's** famous spot paintings.

## Reference image:
![Example Output](reference-image.jpg)

## 📌 Features
- Extracts colors from an image (`image.jpeg`) using `colorgram`
- Uses `turtle` graphics to create a dot painting
- Generates a grid of colorful dots randomly picked from the extracted colors

## 🛠️ Installation:

### 1️⃣ Clone the Repository:

    git clone https://github.com/MatanKaufman1/Hirst-painting.git
    cd Hirst-painting

2️⃣ Install Dependencies:

Make sure you have Python 3 installed, then install the required libraries:

    pip install colorgram.py

## 🚀 How to use:
1️⃣ Place an Image

Add an image named image.jpeg in the project directory. This image will be used to extract colors.
2️⃣ Run the Program

    python main.py

A window will open, displaying the Hirst-style dot painting.

📝 Project Structure:

    Hirst-painting/
    │── colorsExtract.py   # Extracts colors from the image
    │── main.py            # Generates and displays the dot painting
    │── image.jpeg         # Source image for color extraction
    │── README.md          # Project documentation

🎯 Example Output:
Here is an example of the generated Hirst-style dot painting

The program creates an artistic dot pattern like this:

![Example Output](example.png)



📌 Customization

    Change NUM_OF_COLORS in colorsExtract.py to extract more or fewer colors.
    Modify the number_of_dots variable in main.py to create a larger or smaller painting.
    Adjust dot size and spacing by changing:

    arrow.dot(19, random.choice(colors_list))  # Dot size
    arrow.forward(25)  # Spacing between dots

🤝 Contributing

Feel free to fork the repository and make improvements! Open an issue if you find a bug or have suggestion
