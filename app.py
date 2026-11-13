#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

bool game(int randy) {
    std::cout << "Guess: ";
    int Guess;
    std::cin >> Guess;
   
    if (Guess == randy)
    {
        std::cout << "wowie you won";
        return true;
    } else if (Guess < randy)
    {
        std::cout << "too low" << "\n";
       
    } else if (Guess > randy)
    {
        std::cout << "too high" << "\n";
    }
    return false;
}

int main() {
    std::srand(std::time(nullptr));

    int min = 1;
    int max = 100;
   
    int rand_number = (rand() % (max - min + 1)) + min;
   
    while (true) {
        if (game(rand_number)) {
            std::cout << "do you wanna do it again (1 = yes, 2 = no) ";
            int ans;
            std::cin >> ans;
            if (ans == 1) {
                main();
            } else if (ans == 2) {
                std::cout << "ok";
                break;
            }
        }
    }
   
    return 0;
}
