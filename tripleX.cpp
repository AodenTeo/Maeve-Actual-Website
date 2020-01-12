#include <iostream>
#include <ctime>

void PrintIntroduction(int Difficulty)
{
    std::cout << std::endl;
    std::cout << "You are a secret agent breaking into a  level " << Difficulty;
    std::cout << " server room...\n";
    std::cout << "Your mission is to break into the server room without getting caught...\n";
    std::cout << "You need to enter the correct code to continue on...";
}

bool PlayGame(int Difficulty)
{
    PrintIntroduction(Difficulty);
     
    //Declare 3 number code
    const int CodeA = rand() % Difficulty + Difficulty;
    const int CodeB = rand() % Difficulty + Difficulty;
    const int CodeC = rand() % Difficulty + Difficulty;

    const int CodeSum = CodeA + CodeB + CodeC;
    const int CodeProduct = CodeA * CodeB * CodeC;

    //Print sum to the terminal
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << "MISSION " << Difficulty;
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << "Your Intelligence indicates that there are three numbers in the first code...\n";
    std::cout << "The first code adds up to "; 
    std::cout << CodeSum;

    //Print product to the terminal
    std::cout << std::endl;
    std::cout << "and it also has a product of ";
    std::cout << CodeProduct;
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << "(Please note that each number in your code should be seperated by a space in order for the game to run)";
    std::cout << std::endl;
    std::cout << "Please enter the correct code in the space below: ";
    std::cout << std::endl;
    std::cout << std::endl;

    //Store player guess
    int GuessA, GuessB, GuessC;
    std::cin >> GuessA;
    std::cin >> GuessB;
    std::cin >> GuessC;
    std::cout << std::endl;
    std::cout << "You entered the code: ";
    std::cout << GuessA << GuessB << GuessC;
    std::cout << std::endl;
    std::cout << std::endl;

    int GuessSum = GuessA + GuessB + GuessC;
    int GuessProduct = GuessA * GuessB * GuessC;

    //Check if players guess is correct
    if (GuessSum == CodeSum && GuessProduct == CodeProduct)
    {
        std::cout << "Hooray! you typed in the correct code!";
        std::cout << std::endl;
        std::cout << "You have succesfully extracted a file";
        std::cout << std::endl;
        std::cout << "Keep going!";
        std::cout << std::endl;
        return true;
    }
    else
    {
        std::cout << "Oh no! You put in the wrong code!";
        std::cout << std::endl;
        std::cout << "Careful agent! Try again!";
        std::cout << std::endl;
        return false;
    }
}

int main()
{
    srand(time(NULL));
    
    std::cout << std::endl;
    int LevelDiffficulty = 1;
    int const MaxDifficulty = 5;
    while(LevelDiffficulty <= MaxDifficulty)
    {
        std::cout << rand() % 4;
        bool blevelComplete = PlayGame(LevelDiffficulty);
        std::cin.clear();//Clear any errors
        std::cin.ignore();//Discards the buffer


        if(blevelComplete)
        {
            ++LevelDiffficulty;
        }
    }
    std::cout << "Great work agent! You got all the files! Now, get out of there while you still can!";
    std::cout << std::endl;
    return 0;
}
