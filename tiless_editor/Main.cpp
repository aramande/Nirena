/*****************************************************************************************
/* Desc: No-tile editor tutorial
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

#include "CIndieLib.h"
#include "Resources.h"
#include "Map.h"
#include "Listener.h"

/*
==================
Main
==================
*/
int IndieLib()		
{
	// ----- IndieLib intialization -----

	CIndieLib *mI = CIndieLib::Instance();
	if (!mI->Init ()) return 0;	

	// ----- Editor classes initialization -----

	// Resource loading
	Resources mResources;
	char mPath [MAX_PATH];
	GetCurrentDirectory (MAX_PATH, mPath);				// Get the path to the current directory
	strcat (mPath, "\\resources\\tileset_01.xml");		// Add the name of the tileset to the path
	if (!mResources.LoadResources (mPath)) exit (0);

	// Map initialization
	Map mMap;

	// Listener initialization
	Listener mListener (&mResources, &mMap);

	// ----- Main Loop -----

	while (!mI->Input->OnKeyPress (IND_ESCAPE) && !mI->Input->Quit())
	{
		// ----- Input Update ----

		mI->Input->Update ();

		// -------- Atributes -------

		mListener.Listen ();

		// -------- Render -------

		// Reset the counting of rendered and discarded objects
		mI->Render->ResetNumDiscardedObjects();
		mI->Render->ResetNumRenderedObject();

		mI->Render->BeginScene ();

		// Render banckground (two triangles)
		mI->Render->BlitColoredTriangle (0, 0, mI->Window->GetWidth(), 0, 0, mI->Window->GetHeight(), 
										255, 128, 128, 
										255, 128, 128, 
										27, 27, 204,
										255);

		mI->Render->BlitColoredTriangle (0, mI->Window->GetHeight(), mI->Window->GetWidth(), 0, mI->Window->GetWidth(), mI->Window->GetHeight(), 
										27, 27, 204, 
										255, 128, 128, 
										27, 27, 204,
										255);

		// --- Render parallax layer B ---

		mI->Render->SetCamera2d (mListener.GetCameraB());
		mI->Entity2dManager->RenderEntities2d (0);

		// --- Render parallax layer N ---

		mI->Render->SetCamera2d (mListener.GetCameraN());
		mI->Entity2dManager->RenderEntities2d (1);

		// --- Render parallax layer M ---

		mI->Render->SetCamera2d (mListener.GetCameraM());
		mI->Entity2dManager->RenderEntities2d (2);

		// --- Render backdrop elements of Layers from 1 to 9 ---

		mI->Render->SetCamera2d (mListener.GetCameraLayers());

		for (int i = 3; i < NUM_EDITOR_LAYERS; i++)
			mI->Entity2dManager->RenderEntities2d (i);

		// --- Render editor elements (like the brush and areas) ---

		// If editing mode
		if (mListener.GetMode())
		{
			switch (mListener.GetCurrentLayer())
			{
				case 0:		mI->Render->SetCamera2d (mListener.GetCameraB());		break;
				case 1:		mI->Render->SetCamera2d (mListener.GetCameraN());		break;
				case 2:		mI->Render->SetCamera2d (mListener.GetCameraM());		break;
				default:	mI->Render->SetCamera2d (mListener.GetCameraLayers());	break;
			}

			// Render
			mI->Entity2dManager->RenderEntities2d (BRUSH_LAYER);

			// Render the collision areas of the working layer
			mI->Entity2dManager->RenderCollisionAreas (mListener.GetCurrentLayer(), 255, 255, 255, 30);
			mI->Entity2dManager->RenderGridAreas (mListener.GetCurrentLayer(), 255, 0, 0, 255);
		}

		// --- Render texts ---

		// Render gui elements (text, mouse cursor)
		mI->Render->SetCamera2d (mListener.GetCameraGui());
		mI->Entity2dManager->RenderEntities2d (GUI_LAYER);	

		// --- End Scene ---

		mI->Render->EndScene ();

		//mI->Render->ShowFpsInWindowTitle();
	}

	// ----- Free memory (we don't use destructors becase IndieLib pointers would be pointing to null -----

	mListener.Free ();
	mResources.Free ();
	mMap.Free ();

	// ----- Indielib End -----

	mI->End ();

	return 0;
}
