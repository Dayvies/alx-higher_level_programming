#!/usr/bin/node

exports.nbOccurences = function (list, search) {
        let count = 0;
        for (let i = 0; i < list.length; i++) {
          if (search === list[i]) { count += 1; }
        }
        return count;
      };
      