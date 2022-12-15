#!/bin/bash
# catch me if you can
curl 0.0.0.0:5000/catch_me -X PUT -sL -d"user_id=98" -H"Origin: You got me!"
