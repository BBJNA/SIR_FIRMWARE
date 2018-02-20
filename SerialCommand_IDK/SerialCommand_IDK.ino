String command, key, info, buffer;
int x = 50, y = 50, freq = 1000;

void setup(){

  Serial.begin(9600);

}

void loop(){
  //Serial.println(getconfig());
  command = "";
  key = "";
  buffer = "";

  if(Serial.available()){

    command = Serial.readString();

  }

  if(command == "gridx"){
    while(key != "check"){
      Serial.println("Y\n");
      if(Serial.available()){
        key = Serial.readString();
      }
      x = key.toInt();
    }
  }
  
  if(command == "gridy"){
    while(key != "check"){
      Serial.println("Y\n");
      while(Serial.available()>0){
          int inChar = Serial.read();
          if(isDigit(inChar)){
            buffer += (char)inChar;
          }
          if(inChar == '\n'){
              y = buffer.toInt();
              Serial.println(buffer.toInt());
          }
        }
      }
    }
  }

  if(command == "info"){
    while(key != "check"){
      if(Serial.available()){
        key = Serial.readString();
      }
        Serial.println(getconfig());
        delay(100);
    }
  }
}

String getconfig(){
  info = "Gridx = ";
  info += x;
  info += " Gridy = ";
  info += y;
  info += " Freq = ";
  info += freq;
  info += "\n";
  return info;
}

