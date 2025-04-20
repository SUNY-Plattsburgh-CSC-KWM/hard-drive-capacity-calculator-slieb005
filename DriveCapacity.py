def main():
  #prompt for input frrom user
  print("Enter number of platters: ")
  platters = int(input())
  print("Enter number of surfaces per platter: ")
  surfaces = int(input())
  print("Enter number of tracks per surface: ")
  tracks = int(input())
  print("Enter number of sectors per track: ")
  sectors = int(input())
  print("Enter number of bytes per sector: ")
  bytes = int(input())

  #calc total size
  total_bytes = int(platters * surfaces * tracks * sectors * bytes)
  
  kb = total_bytes / 1024 #calc size in kb
  mb = kb / 1024 #calc size in mb
  gb = mb/1024 #calc size in gb
  tb = gb / 1024 #calc size in tb

  #output correct unit
  if tb > 1.0:
    print(f"Drive size: {tb:.1f} TB")
  elif gb > 1.0:
    print(f"Drive size: {gb:.1f} GB")
  elif mb > 1.0:
    print(f"Drive size: {mb:.1f} MB")
  elif kb > 1.0:
    print(f"Drive size: {kb:.1f} KB") 
  else:
    print(f"Drive size: {total_bytes:.1f} bytes")

if __name__ == "__main__":
  main()
