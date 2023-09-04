#include<iostream>
using namespace std;

class student{
public:
	int roll,lic;
	char dob[10];
	char bloodgrp[10];
	char name[20];
	char college[20];
	static int password;
	int display();
	
	student(){
	cout<<"Enter the Name Of Student";
	cin>>name;
	cout<<"Enter the Name Of College";
	cin>>college;
	cout<<"Enter the Roll No Of Student";
	cin>>roll;
	cout<<"Enter the Lic No Of Student";
	cin>>lic;
	cout<<"Enter the DOB Of Student";
	cin>>dob;
	cout<<"Enter the Blood Grp Of Student";
	cin>>bloodgrp;
	cout<<"\n\n\n";
}
~student(){

cout<<endl<<"This Is a Destructor"<<endl;


}
static void staticfun()
    {
   	
        cout << "This Is a static function"<<endl;
        cout<<"This is static variable Password : "<< password << endl;
    }
};





inline int student::display(){
	cout<<"Name Of Student"<<": "<<name<<endl;
	
	cout<<" \n "<<"Name Of College"<<": "<<college<<endl;
	
	cout<<" \n "<<"Roll No Of Student"<<": "<<roll<<endl;
	
	cout<<" \n "<<"Lic No Of Student"<<": "<<lic<<endl;

	cout<<" \n "<<"DOB Of Student"<<": "<<dob<<endl;
		
	cout<<" \n "<<"Blood Grp Of Student"<<": "<<bloodgrp<<endl;
	staticfun();
	
}
int student::password = 0;

int main(){
	int n;
	cout<<"Enter The No of Students";
	cin>>n;
	for(int i=1; i<=n; i++){
	student s1;

	int setpass = 0;
   	cout<<endl<<"Set Password : ";
    	cin>>setpass;
	student::password = setpass;
	cout<<"  "<<"INFO OF STUDENT :"<<i<<endl;
	s1.display();


	}
	
	return 0;
	
}


