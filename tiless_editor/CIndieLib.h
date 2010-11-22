/*****************************************************************************************
/* Desc: IndieLib singleton initialization class
/*
/* gametuto.com - Javier López López (javilop.com)
/*
/*****************************************************************************************
/*
/* Creative Commons - Attribution 3.0 Unported
/* You are free:
/*	to Share — to copy, distribute and transmit the work
/*	to Remix — to adapt the work
/*
/* Under the following conditions:
/* Attribution. You must attribute the work in the manner specified by the author or licensor 
/* (but not in any way that suggests that they endorse you or your use of the work).
/*
/*****************************************************************************************/

#ifndef _CINDIELIB_
#define _CINDIELIB_

#pragma comment (lib, "common/IndieLib_vc2008.lib")
#include "common/LibHeaders/Indie.h"


// --------------------------------------------------------------------------------
//					    	IndieLib initialization class
// --------------------------------------------------------------------------------

class CIndieLib 
{
public:
	
	static CIndieLib* Instance();

	bool Init ();
	void End ();

	// ----- IndieLib objects -----

	IND_3dMeshManager		*MeshManager;
	IND_Input				*Input;
	IND_Window				*Window;
	IND_Render				*Render;
	IND_LightManager		*LightManager;
	IND_ImageManager		*ImageManager; 
	IND_SurfaceManager		*SurfaceManager;
	IND_AnimationManager	*AnimationManager;
	IND_FontManager			*FontManager;
	IND_Entity2dManager		*Entity2dManager;
	IND_Entity3dManager		*Entity3dManager;
	IND_Math				*Math;

protected:

	CIndieLib()  {}
	CIndieLib(const CIndieLib&);
	CIndieLib& operator = (const CIndieLib&);

private:

	static CIndieLib *pinstance;
	void ResetCurrentDirectory_W( void );
};


#endif // _CINDIELIB_
