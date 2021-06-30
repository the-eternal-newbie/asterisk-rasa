extensions = {
  ["internal"] = {
    ["_1XX"] = function (context, extension)
      app.dial('SIP/'..extension);

      local dialstatus = channel["DIALSTATUS"]:get();
      if dialstatus == 'BUSY' then
        -- do something.......
      elseif dialstatus == 'CHANUNAVAIL' then
          -- do another thing
          end;
      end;
  }
}
