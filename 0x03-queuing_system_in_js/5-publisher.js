import { createClient, print } from "redis";

const redis = createClient();

redis
  .on("connect", () => {
    console.log("Redis redis connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis redis not connected to the server: ${error}`);
  });

const publishMessage = (message, time) => {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        redis.publish("holberton school channel", message)
    }, time)
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
