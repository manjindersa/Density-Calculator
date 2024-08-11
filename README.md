# Density Calculator

## Description

The `Density Calculator` is a simple Python program that calculates the density of various objects based on their mass and volume. The program takes a dictionary of objects with their corresponding mass and volume, computes the density for each object, and returns a new dictionary with the calculated densities rounded to three decimal places.

## Files

- `main.py`: The main Python file containing the program logic.

## Usage

1. **Clone the Repository**: Clone the repository to your local machine.
    ```sh
    git clone https://github.com/manjindersa/Density-Calculator.git
    ```
2. **Navigate to the Directory**: Change to the directory containing the files.
    ```sh
    cd Density-Calculator
    ```
3. **Run the Program**: Execute the program to see the output.
    ```sh
    python main.py
    ```

## Functionality

- **`calculate_density(objects)`**: This function takes a dictionary where the keys are object names and the values are tuples containing mass and volume. It calculates the density (mass/volume) for each object and returns a new dictionary with the calculated densities rounded to three decimal places.

### Output
When the `main.py` script is executed, it will output:

```
Original Dictionary:
 {'Box1': (433, 200), 'Box2': (350, 120), 'Box3': (289, 123), 'Box4': (430, 250), 'Box5': (350, 200)}

New Dictionary with density:
 {'Box1': 2.165, 'Box2': 2.917, 'Box3': 2.351, 'Box4': 1.72, 'Box5': 1.75}
```

## Author
- **Manjinder Singh**
- **GitHub**: [manjindersa](https://github.com/manjindersa)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
