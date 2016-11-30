/*
  * Class: CMSC140
 CRN: 20873
 Name: Rahul Shah
 Instructor: Gary C. Thai
 Project 6A
 Date: 11/29/16
  
 I pledge that I have completed the programming assignment independently.
    I have not copied the code from a student or any source.
    I have not given my code to any student.
  
 */

#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;


//file variables

ifstream infile;
ofstream outfile;

//tries to read from the input file and splits it into the arrays
int readInventory(string i[], double p[], string t[]){
    string fileName;
    cout << "Please enter the name of the input file: " << endl;
    cin >> fileName;
    infile.open(fileName);
    
    if (infile){
        //read in to arrays
        for(int c = 0; c < 20; c++){
            for(int k = 1; k <= 3; k++){
                if(k==1)
                    infile >> i[c];
                else if(k ==2)
                    infile >> p[c];
                else
                    infile >> t[c];
            }
        }
    }else{
        cout << "nope" << endl;
        return -1;
    }
    
    infile.close();
    
    return 0; //return one if successfully read in
}

//gets the customers order
void processOrder(string i[], double p[], string t[]){
    //variables
    double tax, total;
    
    //arrays to hold the indexes of the items ordered (in taxable and not taxable types)
    int taxable[20], notTaxable[20];
    
    cout << "Enter the ID of the item you wish to order" << endl;
}

int main() {
    
    //three parallel arrays
    string itemName[20];
    double price[20];
    string isTax[20];
    
    if(readInventory(itemName, price, isTax) == 0){
        //call processOrder(3 arrays)
    }
    
    
    return 0;
}





