#include "mbed.h"
DigitalOut led1(LED1);
UnbufferedSerial      my_pc(USBTX, USBRX);
char data;
void ISR_my_pc_reception(void);
int main()
{    
    my_pc.baud(115200);
    my_pc.attach(&ISR_my_pc_reception, UnbufferedSerial::RxIrq);
    while (true){}
}
void ISR_my_pc_reception(void){
    my_pc.read(&data, 1);     // get the received byte
    if(data == 'a'){    led1 = 1;   } 
    if(data == 'e'){    led1 = 0;   }    
    my_pc.write(&data, 1);    // echo of the byte received
}