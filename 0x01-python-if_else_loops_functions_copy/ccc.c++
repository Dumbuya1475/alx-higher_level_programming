#include <iostream>
#include <cmath>
#include <chrono>
#include <thread>
using namespace std;

#define PI 3.14159

class Calculator
{
public:
    int fnum;
    int snum;
    double result;
    double angle;

    Calculator()
    {
        // Default constructor
    }

    void getdata()
    {
        // Prompt the user to enter two numbers
        cout << "Enter the First number: ";
        cin >> fnum;
        cout << "Enter the second number: ";
        cin >> snum;
    }

    void division()
    {
        // Perform division
        getdata();
        if (snum == 0)
        {
            cout << "Number cannot be divided by zero!!!" << endl;
        }
        else
        {
            result = fnum / snum;
            cout << fnum << " / " << snum << " = " << result << endl;
        }
    }

    void mul()
    {
        // Perform multiplication
        getdata();
        result = fnum * snum;
        cout << fnum << " x " << snum << " = " << result << endl;
    }

    void sub()
    {
        // Perform subtraction
        getdata();
        result = fnum - snum;
        cout << fnum << " - " << snum << " = " << result << endl;
    }

    void add()
    {
        // Perform addition
        getdata();
        result = fnum + snum;
        cout << fnum << " + " << snum << " = " << result << endl;
    }

    void exponent()
    {
        // Calculate exponentiation
        double base, exponent;
        cout << "Enter the base number: ";
        cin >> base;
        cout << "Enter the exponent: ";
        cin >> exponent;
        double result = pow(base, exponent);
        cout << base << " raised to the power of " << exponent << " = " << result << endl;
    }

    void square_root()
    {
        // Calculate square root
        int n1;
        float n2;
        cout << "Enter the number whose square root you want to find: ";
        cin >> n1;
        n2 = sqrt(n1);
        cout << "The square root of " << n1 << " is: " << n2 << endl << endl;
    }

    void Sin()
    {
        // Calculate sine
        cout << "Enter an angle in degrees: ";
        cin >> angle;
        double radians = angle * M_PI / 180.0;
        double sine = sin(radians);
        cout << "Sine: " << sine << endl;
    }

    void Cos()
    {
        // Calculate cosine
        cout << "Enter an angle in degrees: ";
        cin >> angle;
        double radians = angle * M_PI / 180.0;
        double cosine = cos(radians);
        cout << "Cosine: " << cosine << endl;
    }

    void Tan()
    {
        // Calculate tangent
        cout << "Enter an angle in degrees: ";
        cin >> angle;
        double radians = angle * M_PI / 180.0;
        double tangent = tan(radians);
        cout << "Tangent: " << tangent << endl;
    }

    void InverSin()
    {
        // Calculate inverse sine
        double value;
        cout << "Enter a value for inverse sine: ";
        cin >> value;
        double inverseSine = asin(value) * 180.0 / M_PI;
        cout << "Inverse Sine: " << inverseSine << " degrees" << endl;
    }

    void InverCos()
    {
        // Calculate inverse cosine
        double value;
        cout << "Enter a value for inverse cosine: ";
        cin >> value;
        double inverseCosine = acos(value) * 180.0 / M_PI;
        cout << "Inverse Cosine: " << inverseCosine << " degrees" << endl;
    }

    void InverTan()
    {
        // Calculate inverse tangent
        double value;
        cout << "Enter a value for inverse tangent: ";
        cin >> value;
        double inverseTangent = atan(value) * 180.0 / M_PI;
        cout << "Inverse Tangent: " << inverseTangent << " degrees" << endl;
    }

    void Log()
    {
        // Calculate logarithm
        double value;
        cout << "Enter a value for logarithm: ";
        cin >> value;
        double logarithm = log(value);
        cout << "Logarithm: " << logarithm << endl;
    }

    void Log10()
    {
        // Calculate logarithm with base 10
        double value;
        cout << "Enter a value for logarithm with base 10: ";
        cin >> value;
        double logarithmBase10 = log10(value);
        cout << "Logarithm (Base 10): " << logarithmBase10 << endl;
    }
};

int main()
{
    string quest;
    int ch;
    Calculator calc;

    cout << "******************************* Programming Calculator **************************************\n";
    this_thread::sleep_for(chrono::seconds(5));
    cout << "LOADING........................STARTING...............................................\n";
    this_thread::sleep_for(chrono::seconds(3));
    cout << "STARTED\n";
    system("cls");

    while (true)
    {
        cout << "\t\t" << "#############################" << endl;
        cout << "\t\t" << "# WELCOME TO C++ CALCULATOR #" << endl;
        cout << "\t\t" << "#############################" << endl;

        cout << "+-------------------+-----------------+----------------------+\n";
        cout << "+ 1. Division       + 7. Sin          + 13. Log              +\n";
        cout << "+ 2. Multiplication + 8. Cos          + 14. Log with base 10 +\n";
        cout << "+ 3. Subtraction    + 9. Tan          +                      +\n";
        cout << "+ 4. Addition       + 10. Inverse Sin +                      +\n";
        cout << "+ 5. Exponent       + 11. Inverse Cos +                      +\n";
        cout << "+ 6. Square root    + 12. Inverse Tan +                      +\n";
        cout << "+ 0. Exit           +                 +                      +\n";
        cout << "+-------------------+-----------------+----------------------+\n";
        cout << "Enter the function you want to perform: ";
        cin >> ch;

        switch (ch)
        {
            case 1:
                calc.division();
                break;
            case 2:
                calc.mul();
                break;
            case 3:
                calc.sub();
                break;
            case 4:
                calc.add();
                break;
            case 5:
                calc.exponent();
                break;
            case 6:
                calc.square_root();
                break;
            case 7:
                calc.Sin();
                break;
            case 8:
                calc.Cos();
                break;
            case 9:
                calc.Tan();
                break;
            case 10:
                calc.InverSin();
                break;
            case 11:
                calc.InverCos();
                break;
            case 12:
                calc.InverTan();
                break;
            case 13:
                calc.Log();
                break;
            case 14:
                calc.Log10();
                break;
            case 0:
                cout << "Goodbye!" << endl;
                exit(0);
            default:
                cout << "Invalid input. Please try again." << endl;
                break;
        }

        cout << endl;

        cout << "Do you want to Clear Screen (yes/no)? ";
        cin >> quest;
        if (quest == "yes")
        {
            system("cls");
        }
    }

    return 0;
}