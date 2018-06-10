String data;

void setup(){
   Serial.begin(9600);
   for(int i = 0; i <= 13; i++){
       pinMode(i, OUTPUT);
       digitalWrite(i, LOW);
   }
}

String getValue(String data, char separator, int index)
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void loop(){
    while(Serial.available() > 0){
        data = Serial.readString();
        String action = getValue(data, '-', 0);
        Serial.println(data);
        if(action == "ON"){
            String pin_str = getValue(data, '-', 1);
            int pin_int = pin_str.toInt();
            digitalWrite(pin_int, HIGH);
        } else if (action == "OFF"){
            String pin_str = getValue(data, '-', 1);
            int pin_int = pin_str.toInt();
            digitalWrite(pin_int, LOW);
        }
    }
}