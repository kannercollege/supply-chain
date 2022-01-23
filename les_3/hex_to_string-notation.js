let values = Object.values(msg.payload["uplink_message"]["frm_payload"]);

var track = ""

values.forEach((val,index) => {
    
  if (val.toString(16).length == 1){
      val = "0" + val.toString(16);
  } else{
      val = val.toString(16);
  }

  track = track + val + " "; 
})
msg.payload = track.toUpperCase();
return msg;