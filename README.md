# MSI-RPi
Affordable and Portable Multi-Spectral Imaging based on Raspberry Pi (MSI-RPi) for Plant Phenotype Studies

The general overall flow to be followed to get started is as follows:-

The Multi-Spectral image acquistion scripts are placed in the folder updated_latest_camera_automation_V1/

  1) Click on the "DATA_AQUISTION.desktop" icon to launch the application. 
     Alternately, you can also run the shell script "RUN.sh" on the terminal to launch the program as "sudo bash Run.sh" 
     The images will be acquired from 8am - 6pm with an logging interval of every 30 minutes. This can be changed as per desired in the provided automation script.
     The spectral band images are stored in the folder image/ with the naming conventions as following:-
     
      *     C1_NoIR_550F_%Y%m%d_%H%m%s.png
    
      *     C2_NoIR_1070F_%Y%m%d_%H%m%s.png
    
      *     C3_RGB_%Y%m%d_%H%m%s.png
    
      *     C4_NoIR_725F_%Y%m%d_%H%m%s.png
      
   
 All the image analysis code is provided in the folder notebooks/ along with their respective notebooks

