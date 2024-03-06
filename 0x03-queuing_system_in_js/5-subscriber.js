import { createClient, print } from "redis";

const redis = createClient();

redis
  .on("connect", () => {
    console.log("Redis redis connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis redis not connected to the server: ${error}`);
  });


  redis.subscribe("holberton school channel")
  redis.on("message",  (err, mssg)=> { 
    console.log(mssg);
    if (mssg == "KILL_SERVER") {
        redis.unsubscribe()
        redis.quit()
    }
})

