String command, key, info;
int x = 50, y = 50, tfreq = 1000;

void setup(){

  Serial.begin(9600);

}

void loop(){
  
  command = "";
  key = "";
  
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
      if(Serial.available()){
        key = Serial.readString();
      }
      y = key.toInt();
    }
  }

  if(command == "info"){
    while(key != "check"){
      Serial.println("Y\n");
      if(Serial.available()){
        key = Serial.readString();
      }
      if(key == "conf"){
        Serial.println(getconfig());
      }
    }
  }
}

String getconfig(){
  info = "Gridx = ";
  info += x;
  info += " Gridy = ";
  info += y;
  info += " Freq = ";
  info += tfreq;
  info += "\n";
  return info;
}

