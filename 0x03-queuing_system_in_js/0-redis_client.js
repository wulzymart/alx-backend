import { createClient } from "redis";

const redis = createClient();
redis
  .on("error", (err) =>
    console.log("Redis client not connected to the server: ", err)
  )
  .on("connect", () => {
    console.log("Redis client connected to the server");
  });
