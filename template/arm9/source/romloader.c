#include <nds.h>
#include <stdio.h>
#include <string.h>
#include <dirent.h>
#include <stdlib.h>
#include <unistd.h>
#include "ds_misc.h"
#include "c_defs.h"
#include "minIni.h"
#include "menu.h"

extern int subscreen_stat;
extern int shortcuts_tbl[16];

char tmpname[] = "dszip.tmp";

int romsize;	//actual rom size
int freemem_start;	//points to unused mem (end of loaded rom)
int freemem_end;
u32 oldinput;

char romfilename[256];	//name of current rom.  null when there's no file (rom was embedded)
char *romfileext;	//points to file extension

//extern u8 autostate;			//from ui.c
int active_interface = 0;

void rommenu(int roms);
void drawmenu(int sel,int roms);
int getinput(void);

int init_rommenu(void);
void listrom(int line,int rom,int highlight); //print rom title
int loadrom(int rom);	//return -1 on success, or rom count (from directory change)
void stringsort(char**);

extern int argc;
extern char **argv;
char inibuf[768];
char ininame[768];

