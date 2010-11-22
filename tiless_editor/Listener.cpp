/*****************************************************************************************
/* Desc: Listener class, interface between the user and the editor using keyboard and
/* mouse Input
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

// ------ Includes -----

#include "Listener.h"

/* 
======================================									
Init
====================================== 
*/
Listener::Listener(Resources *pResources, Map *pMap) 
{
	// Get IndieLib instante
	mI = CIndieLib::Instance();

	// Classes
	mResources = pResources;
	mMap = pMap;

	// Screen dimensions and fullscreen flag
	mScreenWidth = mI->Window->GetWidth();
	mScreenHeight = mI->Window->GetHeight();

	// Backdrop
	mBackDropNodeOver			= 0;			// The mouse cursor is over this backdrop
	mIsRotatingBackDrop		= false;			// Flag used when rotating a backdrop
	mIsTranslatingBackDrop	= false;			// Flag used when translating a backdrop
	mIsScalingBackDrop		= false;			// Flag used when scaling a backdrop
	mIsTintingBackDrop		= false;			// Flag used when tinting a backdrop

	// Text showed
	mText [0] = 0;		

	// Init mode = editing
	mMode =		true;							// Editing / In game
	strcpy (mModeName, "Editing mode  |  ");

	// All the backdrop objects in this editor are on one of 13 layers.
	// The first 3 layers are parallax layers, mapped to "B", "N" and "M" keys in they 
	// keyboard.
	//
	// The following nine layers are mapped to the 1-9 keys. Layers 8-9 are the only layers that 
	// go over active entities, like the main player!
	//
	// The final layer is the "dark layer", layer mapped to "J". Is another layer that you
	// could use in order to draw semi-translucent dark sprites in order to simulate darkness.
	// 
	// For coding all this in the editor we only need a variable called mLayer that stores
	// the number of the layer we are working on. Later, when dropping a piece, we just have
	// to check in which layer we are working and to add the IndieLib entity of the dropped node
	// to the proper layer user IndieLib Entity2dManger class, that let you choose in which layer
	// you want to add an entity. Later, in the main loop, we just render each layer, starting
	// from 0 to the last layer, using Entity2dManger::RenderEntities2d() method.
	//
	// On the following list you can see in the first colum the number for coding the layer 
	// and in the second colum its real name.  Don't make a mistake thinking for example 
	// than the layer named "1" is coded in mLayer variable as 1:
	//
	// 0	= b
	// 1	= n
	// 2	= m
	// 3-11 = 1-9
	// 12	= j
	mLayer =	3;	// (Layer 1)
	strcpy (mLayerName, "Layer 1 (Tiled surfaces)");

	// Camera initialization (middle of the screen area)
	mCameraLayersX = mCameraBX = mCameraNX = mCameraMX = (float) mI->Window->GetWidth () / 2;
	mCameraLayersY = mCameraBY = mCameraNY = mCameraMY = (float) mI->Window->GetHeight () / 2;

	// We use 4 cameras, one for each parallax scroll and one for the rest of layers
	mCameraB = new IND_Camera2d ((int) mCameraLayersX, (int) mCameraLayersY);
	mCameraN = new IND_Camera2d ((int) mCameraLayersX, (int) mCameraLayersY);
	mCameraM = new IND_Camera2d ((int) mCameraLayersX, (int) mCameraLayersY);
	mCameraLayers = new IND_Camera2d ((int) mCameraLayersX, (int) mCameraLayersY);
	mCameraGui = new IND_Camera2d ((int) mCameraLayersX, (int) mCameraLayersY);

	// Set the camera zoom
	ResetZoom ();

	// Create the backdrop entities that are used to show on the screen which backdrop
	// sprite is currently as a brush and ready to be dropped.
	CreateBackDropBrushes ();
}


/* 
======================================									
Free memory
====================================== 
*/
void Listener::Free ()
{
	// Free cameras
	delete mCameraB;
	delete mCameraN; 
	delete mCameraM; 
	delete mCameraLayers;
	delete mCameraGui;

	// Delete Brushes
	DeleteBackDropBrushes ();
}


/* 
======================================									
Get the input from keyboard and mouse and calls to the appropiate methods. This class takes care of
every action that the user calls.
====================================== 
*/
void Listener::Listen()
{
	// Input that is the same for "editing" and "in game" modes
	ListenCommon ();

	// Get input for the appropiate mode
	if (mMode)
		// Input for "editing" mode
		ListenEditing();
	else
		// Input for "in game" mode
		ListenInGame();
}


// --------------------------------------------------------------------------------
//									Private methods
// --------------------------------------------------------------------------------

/* 
======================================									
Getting input for actions that are the same for "editing mode" and "in game mode"
====================================== 
*/
void Listener::ListenCommon()
{
	// -------------------- Text --------------------

	// Update info-text
	strcpy (mText, mModeName);

	// -------------------- Time measurement --------------------

	mDelta = mI->Render->GetFrameTime() / 1000.0f;

	// -------------------- Get mouse position --------------------

	mMouseX = mI->Input->GetMouseX();
	mMouseY = mI->Input->GetMouseY();

	// -------------------- Update IndieLib cameras  --------------------

	// Update the position of the cameras
	mCameraB->SetPosition		((int) mCameraBX, (int) mCameraBY);
	mCameraN->SetPosition		((int) mCameraNX, (int) mCameraNY);
	mCameraM->SetPosition		((int) mCameraMX, (int) mCameraMY);
	mCameraLayers->SetPosition	((int) mCameraLayersX, (int) mCameraLayersY);

	// Update the zoom factor of the cameras
	mCameraB->SetZoom			(mCameraZoomB);
	mCameraN->SetZoom			(mCameraZoomN);
	mCameraM->SetZoom			(mCameraZoomM);
	mCameraLayers->SetZoom		(mCameraZoomLayers);

	// -------------------- Switch between "editing" and "in game" mode when pressing tab --------------------

	if (mI->Input->OnKeyRelease (IND_TAB)) 
	{
		if (mMode)				
		{
			strcpy (mModeName, "In game mode");					// Set text		
			if (mBackDropNodeOver) mBackDropNodeOver->GetEntity()->ShowGridAreas (false);
			mMode = false;
		}
		else
		{
			strcpy (mModeName, "Editing mode  |  ");			// Set text
			mMode = true;
		}
	}

	// -------------------- Save Map --------------------

	if (mI->Input->IsKeyPressed (IND_LCTRL) && mI->Input->OnKeyPress (IND_S))
		mMap->SaveMap (mResources->GetTilesetPath());

	// -------------------- New Map --------------------

	if (mI->Input->IsKeyPressed (IND_LCTRL) && mI->Input->OnKeyPress (IND_N))
	{
		char *mTilesetPath = mMap->GetPathToTileset ();
		if (mTilesetPath)
		{
			// We try to load a new tileset
			if (mResources->LoadTileset (mTilesetPath))
			{
				DeleteBackDropBrushes();			// Delete old brushes. TODO-> Check is the tileset is already loaded
				CreateBackDropBrushes();			// Create the new brushes using the new loaded tileset
				mMap->FreeMap();					// Free old map
			}
			else	
				exit (0);							// Just exit if we can't load it: TODO -> Show a message
		}
	}

	// -------------------- Load Map --------------------

	if (mI->Input->IsKeyPressed (IND_LCTRL) && mI->Input->OnKeyPress (IND_L))
	{
		// Try to load the map
		if (mMap->LoadMap (mResources))
		{
			DeleteBackDropBrushes();				// Delete old brushes. TODO-> Check is the tileset is already loaded
			CreateBackDropBrushes();				// Create the new brushes using the new loaded tileset
		}
		else
			exit (0);								// Just exit if we can't load it: TODO -> Show a message
	}

	// -------------------- Camera position --------------------

	// The camera movement is time dependent, each camera has a different speed

	if (mI->Input->IsKeyPressed	(IND_A))
	{
		mCameraBX		-= CAMERA_SPEED_B		* mDelta;
		mCameraNX		-= CAMERA_SPEED_N		* mDelta;
		mCameraMX		-= CAMERA_SPEED_M		* mDelta;
		mCameraLayersX	-= CAMERA_SPEED_LAYERS	* mDelta;
	}

	if (mI->Input->IsKeyPressed	(IND_D))
	{
		mCameraBX		+= CAMERA_SPEED_B		* mDelta;
		mCameraNX		+= CAMERA_SPEED_N		* mDelta;
		mCameraMX		+= CAMERA_SPEED_M		* mDelta;
		mCameraLayersX	+= CAMERA_SPEED_LAYERS	* mDelta;
	}

	if (mI->Input->IsKeyPressed	(IND_W))
	{
		mCameraBY		-= CAMERA_SPEED_B		* mDelta;
		mCameraNY		-= CAMERA_SPEED_N		* mDelta;
		mCameraMY		-= CAMERA_SPEED_M		* mDelta;
		mCameraLayersY	-= CAMERA_SPEED_LAYERS	* mDelta;
	}

	if (mI->Input->IsKeyPressed	(IND_S))
	{
		mCameraBY		+= CAMERA_SPEED_B		* mDelta;
		mCameraNY		+= CAMERA_SPEED_N		* mDelta;
		mCameraMY		+= CAMERA_SPEED_M		* mDelta;
		mCameraLayersY	+= CAMERA_SPEED_LAYERS	* mDelta;
	}

	// -------------------- Camera zoom --------------------

	// Zoom in
	if (mI->Input->IsKeyPressed	(IND_KEYUP))		
	{	
		mCameraZoomB		+= (DIST_CAMERA_B		* mDelta) / 1000;
		mCameraZoomN		+= (DIST_CAMERA_N		* mDelta) / 1000;
		mCameraZoomM		+= (DIST_CAMERA_M		* mDelta) / 1000;
		mCameraZoomLayers	+= (DIST_CAMERA_LAYERS	* mDelta) / 1000;	
	}

	// Zoom out
	if (mCameraZoomB > 0) // Avoid too much zoom-out 
	{
		if (mI->Input->IsKeyPressed	(IND_KEYDOWN))	
		{
			mCameraZoomB		-= (DIST_CAMERA_B		* mDelta) / 1000;
			mCameraZoomN		-= (DIST_CAMERA_N		* mDelta) / 1000;
			mCameraZoomM		-= (DIST_CAMERA_M		* mDelta) / 1000;
			mCameraZoomLayers	-= (DIST_CAMERA_LAYERS	* mDelta) / 1000;	
		}
	}

	// Reset zoom
	if (mI->Input->OnKeyPress (IND_R)) ResetZoom ();

	// -------------------- Toggle full screen--------------------

	if (mI->Input->OnKeyPress (IND_F1)) 
	{
		// Change to window mode and set Vsync off
		if (mI->Window->IsFullScreen())
			mI->Render->Reset ("", mScreenWidth, mScreenHeight, 32, 0, 0);
		// Change to full screen and set Vsync on
		else
			mI->Render->Reset ("", mScreenWidth, mScreenHeight, 32, 1, 1);
	}

	// -------------------- Change screen resolution --------------------

	if (mI->Input->OnKeyPress (IND_F2)) 
		if (!ResetScreen (640, 480)) exit (0);

	if (mI->Input->OnKeyPress (IND_F3))
		if (!ResetScreen (800, 600)) exit (0);

	if (mI->Input->OnKeyPress (IND_F4))
		if (!ResetScreen (1024, 768)) exit (0);

	if (mI->Input->OnKeyPress (IND_F5))
		if (!ResetScreen (1440, 900)) exit (0);
}


/* 
======================================									
Input for "editing" mode
====================================== 
*/
void Listener::ListenEditing()
{
	// -------------------- Text ------------- 

	strcat (mText, mLayerName);
	mResources->GetFontEntity	()->SetText (mText);

	// -------------------- Brush position ------------- 

	// Here we calculate the position of the brush. We first translate it to the origin (the screen center)
	// then we scale it using the zooming factor. Finally we translate it back to the camera position
	// You should use the zoom and coordiante for the specific layer you are editing // (Fixed by Metadon)

	switch (mLayer)
	{
		case 0:
			mPosBrushX = ( ( mMouseX - (mScreenWidth  / 2) ) * ( 1 / (mCameraB->GetZoom()) ) )  + mCameraB->GetPosX();
			mPosBrushY = ( ( mMouseY - (mScreenHeight / 2) ) * ( 1 / (mCameraB->GetZoom()) ) )  + mCameraB->GetPosY();	
			break;
		case 1:	
			mPosBrushX = ( ( mMouseX - (mScreenWidth  / 2) ) * ( 1 / (mCameraN->GetZoom()) ) )  + mCameraN->GetPosX();
			mPosBrushY = ( ( mMouseY - (mScreenHeight / 2) ) * ( 1 / (mCameraN->GetZoom()) ) )  + mCameraN->GetPosY();
			break;
		case 2:		
			mPosBrushX = ( ( mMouseX - (mScreenWidth  / 2) ) * ( 1 / (mCameraM->GetZoom()) ) )  + mCameraM->GetPosX();
			mPosBrushY = ( ( mMouseY - (mScreenHeight / 2) ) * ( 1 / (mCameraM->GetZoom()) ) )  + mCameraM->GetPosY();
			break;
		default:	
			mPosBrushX = ( ( mMouseX - (mScreenWidth  / 2) ) * ( 1 / mCameraZoomLayers ) )  + mCameraLayersX;
			mPosBrushY = ( ( mMouseY - (mScreenHeight / 2) ) * ( 1 / mCameraZoomLayers ) )  + mCameraLayersY;
			break;
	}

	// Sets mouse position and scale in the brush position
	mResources->GetMouseEntity()->SetPosition	(mPosBrushX, mPosBrushY, 1);
	mResources->GetMouseEntity()->SetScale		(1 / mCameraZoomLayers, 1 / mCameraZoomLayers);


	// -------------------- Check collisions between the mouse an the backdrop images of the current layer --------------------

	// We are currently making a backdrop transformation
	if (mIsTranslatingBackDrop || mIsRotatingBackDrop || mIsScalingBackDrop || mIsTintingBackDrop)
	{
		ListenHoverBackDrop ();
	}
	// Only check collisions if we are not already making a transformation over a backdrop
	else
	{
		// Check a collision between the mouse a node
		Node *mNewBackDropNodeOver = CheckMouseCollisions (mLayer);

		// The cursor is over a backdrop image 
		if (mNewBackDropNodeOver)
		{ 
			// New backdrop
			if (mNewBackDropNodeOver != mBackDropNodeOver)
			{
				if (mBackDropNodeOver)
					mBackDropNodeOver->GetEntity()->ShowGridAreas (false);
				mBackDropNodeOver = mNewBackDropNodeOver;
			}

			// Show red rectangle
			mBackDropNodeOver->GetEntity()->ShowGridAreas (true);

			// Hide backdrop brush 
			mBackDropBrushes [mCurrentBackDropBrush].mEntity.SetShow (false);

			// Listen for possible changes that the selected backdrop can suffer
			ListenHoverBackDrop ();
		}
		// The cursor is not over any backdrop (brush mode por droping images)
		else
		{
			if (mBackDropNodeOver)
				mBackDropNodeOver->GetEntity()->ShowGridAreas (false);

			// Show backdrop brush 
			mBackDropBrushes [mCurrentBackDropBrush].mEntity.SetShow (true);

			// Listen for switching between backdrop images on the brush, drop them in the map, etc
			ListenBackDropBrush ();
		}
	}

	// -------------------- Switch between layers --------------------

	// Parallax layer (b, n, m)
	if (mI->Input->OnKeyPress (IND_B)) ChangeLayer (0, "Layer B (1st Parallax Layer)");
	if (mI->Input->OnKeyPress (IND_N) && !mI->Input->IsKeyPressed (IND_LCTRL)) ChangeLayer (1, "Layer N (2nd Parallax Layer)");
	if (mI->Input->OnKeyPress (IND_M)) ChangeLayer (2, "Layer M (3rd Parallax Layer)");

	// Layers 1-9
	if (mI->Input->OnKeyPress (IND_1)) ChangeLayer (3, "Layer 1 (Tiled surfaces)");
	if (mI->Input->OnKeyPress (IND_2)) ChangeLayer (4, "Layer 2");
	if (mI->Input->OnKeyPress (IND_3)) ChangeLayer (5, "Layer 3");
	if (mI->Input->OnKeyPress (IND_4)) ChangeLayer (6, "Layer 4");
	if (mI->Input->OnKeyPress (IND_5)) ChangeLayer (7, "Layer 5");
	if (mI->Input->OnKeyPress (IND_6)) ChangeLayer (8, "Layer 6");
	if (mI->Input->OnKeyPress (IND_7)) ChangeLayer (9, "Layer 7");
	if (mI->Input->OnKeyPress (IND_8)) ChangeLayer (10, "Layer 8");
	if (mI->Input->OnKeyPress (IND_9)) ChangeLayer (11, "Layer 9");

	// Dark layer (j)
	if (mI->Input->OnKeyPress (IND_J)) ChangeLayer (12, "Layer J (Dark Layer)");
}


/* 
======================================									
Listen for possible changes that the selected backdrop (the one where the cursos is over) can suffer
====================================== 
*/
void Listener::ListenHoverBackDrop ()
{
	static int mMouseClickX;
	static int mMouseClickY;

	IND_Entity2d *mBackDropOver = mBackDropNodeOver->GetEntity();

	// -------------------- Translate the selected backdrop image --------------------

	static float mInitialPosX, mInitialPosY;
	float mNewPosX, mNewPosY;

	if (!mIsRotatingBackDrop && !mIsScalingBackDrop)
	{
		if (mI->Input->OnMouseButtonPress(IND_MBUTTON_LEFT))
		{
			mMouseClickX = (int) mPosBrushX;
			mMouseClickY = (int) mPosBrushY;

			mInitialPosX = mBackDropOver->GetPosX();
			mInitialPosY = mBackDropOver->GetPosY();
		}

		if (mI->Input->IsMouseButtonPressed (IND_MBUTTON_LEFT))
		{
			mNewPosX = mInitialPosX + (mPosBrushX - mMouseClickX);
			mNewPosY = mInitialPosY + (mPosBrushY - mMouseClickY);

			mBackDropOver->SetPosition (mNewPosX, 
										mNewPosY, 
										mBackDropOver->GetPosZ());

			mIsTranslatingBackDrop = true;
		}


		if (mI->Input->OnMouseButtonRelease(IND_MBUTTON_LEFT))
		{
			mIsTranslatingBackDrop = false;
		}
	}

	// -------------------- Translate pixel by pixel --------------------

	if (mI->Input->OnKeyPress	(IND_F))
	{
		mBackDropOver->SetPosition (mBackDropOver->GetPosX() - 1, 
									mBackDropOver->GetPosY(), 
									mBackDropOver->GetPosZ());
	}

	if (mI->Input->OnKeyPress	(IND_G))
	{
		mBackDropOver->SetPosition (mBackDropOver->GetPosX() + 1, 
									mBackDropOver->GetPosY(), 
									mBackDropOver->GetPosZ());
	}

	if (mI->Input->OnKeyPress	(IND_C))
	{
		mBackDropOver->SetPosition (mBackDropOver->GetPosX(), 
									mBackDropOver->GetPosY() - 1, 
									mBackDropOver->GetPosZ());
	}

	if (mI->Input->OnKeyPress	(IND_V))
	{
		mBackDropOver->SetPosition (mBackDropOver->GetPosX(), 
									mBackDropOver->GetPosY() + 1, 
									mBackDropOver->GetPosZ());
	}

	// -------------------- Scale the selected backdrop image --------------------

	static float mInitialScale;
	float mNewScale;
	static int mInitialRegionX, mInitialRegionY;
	int mNewRegionX, mNewRegionY;

	if (!mIsRotatingBackDrop && !mIsTranslatingBackDrop)
	{
		if (mI->Input->OnMouseButtonPress (IND_MBUTTON_RIGHT) && mI->Input->IsKeyPressed (IND_LSHIFT))
		{
			mMouseClickX = (int) mPosBrushX;

			if (!mBackDropOver->IfWrap())
			{
				mInitialScale = mBackDropOver->GetScaleX();
			}
			else
			{
				mInitialRegionX = mBackDropOver->GetRegionWidth();
				mInitialRegionY = mBackDropOver->GetRegionHeight();
			}
		}

		if (mI->Input->IsMouseButtonPressed (IND_MBUTTON_RIGHT) && mI->Input->IsKeyPressed(IND_LSHIFT))
		{
			mIsScalingBackDrop = true;

			if (!mBackDropOver->IfWrap())
			{	
				mNewScale = mInitialScale + ((mPosBrushX - mMouseClickX) / 1000);
				if (mNewScale < 0.05f) mNewScale = 0.1f;
				mBackDropOver->SetScale (mNewScale, mNewScale);
			}
			else
			{
				mNewRegionX = mInitialRegionX + ((int) mPosBrushX - mMouseClickX);
				mNewRegionY = mInitialRegionY + ((int) mPosBrushX - mMouseClickX);
				mBackDropOver->SetRegion	(0, 
											0, 
											(int) mNewRegionX, 
											(int) mNewRegionY);

			}
		}

		if (mI->Input->OnMouseButtonRelease (IND_MBUTTON_RIGHT))
		{
			mIsScalingBackDrop = false;
		}
	}

	// -------------------- Rotate the selected backdrop image --------------------

	static float mInitialAngle;
	float mNewAngle;

	if (!mIsTranslatingBackDrop && !mIsScalingBackDrop)
	{
		if (mI->Input->OnMouseButtonPress (IND_MBUTTON_RIGHT))
		{
			mMouseClickX = (int) mPosBrushX;
			mInitialAngle = mBackDropOver->GetAngleZ();
		}

		if (mI->Input->IsMouseButtonPressed (IND_MBUTTON_RIGHT))
		{
			mNewAngle = mInitialAngle + (mPosBrushX - mMouseClickX);
			mBackDropOver->SetAngleXYZ (0, 0, mNewAngle);
			mIsRotatingBackDrop = true;
		}

		if (mI->Input->OnMouseButtonRelease (IND_MBUTTON_RIGHT))
		{
			mIsRotatingBackDrop = false;
		}
	}

	// -------------------- Flip backdrop image --------------------

	if (mI->Input->OnKeyPress(IND_T))
	{
		(mBackDropOver->GetMirrorX() == true) ? mBackDropOver->SetMirrorX (false) : mBackDropOver->SetMirrorX (true);
	}

	if (mI->Input->OnKeyPress(IND_Y))
	{
		(mBackDropOver->GetMirrorY() == true) ? mBackDropOver->SetMirrorY (false) : mBackDropOver->SetMirrorY (true);
	}

	// -------------------- Transparency --------------------

	if (mI->Input->IsKeyPressed (IND_U, 5))
	{
		int mTrans = mBackDropOver->GetTransparency();
		if (mBackDropOver->GetTransparency() > 0) mBackDropOver->SetTransparency (mBackDropOver->GetTransparency() - 1);
	}

	if (mI->Input->IsKeyPressed (IND_I, 5))
	{
		int mTrans = mBackDropOver->GetTransparency();
		if (mBackDropOver->GetTransparency() < 255) mBackDropOver->SetTransparency (mBackDropOver->GetTransparency() + 1);
	}

	// -------------------- Tiling --------------------

	if (mI->Input->OnKeyPress(IND_L) && !mI->Input->IsKeyPressed (IND_LCTRL))
	{
		(mBackDropOver->IfWrap() == true) ? mBackDropOver->ToggleWrap (false) : mBackDropOver->ToggleWrap (true);
		mBackDropOver->SetRegion	(0, 
									0, 
									mBackDropOver->GetSurface()->GetWidth(), 
									mBackDropOver->GetSurface()->GetHeight());
	}

	// -------------------- Tinting --------------------

	if (mI->Input->IsKeyPressed(IND_SPACE))
	{
		mBackDropOver->SetTint (mMouseX, mMouseY, mMouseX);
		mIsTintingBackDrop = true;
	}

	if (mI->Input->OnKeyRelease(IND_SPACE))
	{
		mIsTintingBackDrop = false;
	}

	// -------------------- Z ordering --------------------

	if (mI->Input->OnKeyPress(IND_Z))
	{
		mBackDropOver->SetPosition (mBackDropOver->GetPosX(), mBackDropOver->GetPosY(), mBackDropOver->GetPosZ() - 1);
	}

	if (mI->Input->OnKeyPress(IND_X))
	{
		mBackDropOver->SetPosition (mBackDropOver->GetPosX(), mBackDropOver->GetPosY(), mBackDropOver->GetPosZ() + 1);
	}

	// -------------------- Clone --------------------

	if (mI->Input->IsKeyPressed(IND_LSHIFT) && mI->Input->OnMouseButtonPress (IND_MBUTTON_LEFT))
	{
		mMap->CloneNode (mBackDropNodeOver);	// Clone node
	}

	// -------------------- Delete --------------------

	if (mI->Input->OnKeyPress(IND_DELETE))
	{
		mMap->DeleteNode (mBackDropNodeOver);	// Erase the node from the map vector
	}
}


/* 
======================================									
Listen for switching between backdrop images, drop them in the map, etc
====================================== 
*/
void Listener::ListenBackDropBrush()
{
	// -------------------- Switch between brush backdrop images (previous) --------------------

	// Switch between brush backdrop images (previous)
	if (mI->Input->OnMouseButtonPress (IND_MBUTTON_WHEELDOWN )) 
	{
		// Hide current backdrop, we are going to change to another one
		mBackDropBrushes [mCurrentBackDropBrush].mEntity.SetShow (false);

		// Set previous backdrop as the current one
		mCurrentBackDropBrush--; 
		if (mCurrentBackDropBrush < 0) mCurrentBackDropBrush = mNumBackDropBrushes - 1;

		// Show current backdrop
		mBackDropBrushes [mCurrentBackDropBrush].mEntity.SetShow (true);
	}

	// Switch between brush backdrop images (next)
	if (mI->Input->OnMouseButtonPress (IND_MBUTTON_WHEELUP )) 
	{
		// Hide current backdrop, we are going to change to another one
		mBackDropBrushes [mCurrentBackDropBrush].mEntity.SetShow (false);

		// Set next backdrop as the current one
		mCurrentBackDropBrush++; 
		if (mCurrentBackDropBrush > mNumBackDropBrushes - 1) mCurrentBackDropBrush = 0;

		// Show current backdrop
		mBackDropBrushes [mCurrentBackDropBrush].mEntity.SetShow (true);
	}

	// -------------------- Updating current backdrop "brush" position --------------------

	// Position of the backdrop brush in the mouse position already calculated in ListenCommon(). 
	mBackDropBrushes [mCurrentBackDropBrush].mEntity.SetPosition (mPosBrushX, mPosBrushY, 0);

	// -------------------- Drop back drop :) --------------------

	if (mI->Input->OnMouseButtonRelease(IND_MBUTTON_LEFT))
	{
		mMap->CreateNode ((int) mPosBrushX, (int) mPosBrushY, 0, mBackDropBrushes [mCurrentBackDropBrush].mId, mLayer, mBackDropBrushes [mCurrentBackDropBrush].mEntity.GetSurface());
	}
}


/* 
======================================									
Input for "in game" mode. This method should be expanded with the game logic
====================================== 
*/
void Listener::ListenInGame()
{
	// -------------------- Text --------------------

	strcat (mText, "\nFps: ");
	strcat (mText, mI->Render->GetFpsString());
	strcat (mText, "\nRendered: ");
	char mDiscardedStr [64];
	itoa (mI->Render->GetNumRenderedObjectsInt() - 43, (char *) &mDiscardedStr, 10);
	strcat (mText, mDiscardedStr);
	strcat (mText, "\nDiscarded: ");
	strcat (mText, mI->Render->GetNumDiscardedObjectsString());
}


/* 
======================================									
Resets screen resolution
====================================== 
*/
bool Listener::ResetScreen (int pScreenWidth, int pScreenHeight)
{
	if (mI->Window->IsFullScreen())
	{
		if (!mI->Render->Reset ("", pScreenWidth, pScreenHeight, 32, 1, 1)) return false;
	}
	else
	{
		if (!mI->Render->Reset ("", pScreenWidth, pScreenHeight, 32, 0, 0)) return false;
	}

	mScreenWidth = pScreenWidth;
	mScreenHeight = pScreenHeight;

	mCameraGui->SetPosition (mScreenWidth / 2, mScreenHeight / 2);

	return true;
}


/* 
======================================									
This method changes the current layer number and name
====================================== 
*/
void Listener::ChangeLayer (int pNumLayer, char *pLayerName)
{
	mLayer = pNumLayer;
	strcpy (mLayerName, pLayerName);
}


/* 
======================================									
Reset zooms
====================================== 
*/
void Listener::ResetZoom ()
{
	mCameraZoomB = 1.0f / ((float) DIST_CAMERA_B / (float) DIST_CAMERA_LAYERS);
	mCameraZoomN = 1.0f / ((float) DIST_CAMERA_N / (float) DIST_CAMERA_LAYERS);
	mCameraZoomM = 1.0f / ((float) DIST_CAMERA_M / (float) DIST_CAMERA_LAYERS);
	mCameraZoomLayers = 1.0f;
}


/* 
======================================		
Check if the mouse is over a backdrop piece and returns the a pointer to the appropiate node
====================================== 
*/
Node *Listener::CheckMouseCollisions (int pLayer)
{
	vector <Node*>::iterator mIter;
	int mCurrentDist = NUM_INFINITE;
	Node *mCandidate = 0;

	// Iterate the vector of backdrop images already loaded and create
	for (mIter  = mMap->GetVectorNodes()->begin();
		mIter !=  mMap->GetVectorNodes()->end();
		mIter++)
	{	
		// Only take in count the backdrops images of the current layer
		if ((*mIter)->GetLayer() == pLayer)
		{
			// Check collision between the mouse cursor and a backdrop image
			if (mI->Entity2dManager->IsCollision ((*mIter)->GetEntity(), "editor", mResources->GetMouseEntity(), "cursor"))
			{
				int mDistToBrush = (int) abs (mPosBrushX - (*mIter)->GetEntity()->GetPosX ());

				if (mDistToBrush < mCurrentDist)  
				{
					mCurrentDist = mDistToBrush;
					mCandidate = (*mIter);
				}
			}
		}
	}

	if (mCandidate)
		return mCandidate;
	

	// If the mouse is not over any backdrop of the current layer it return 0
	return 0;
}


/* 
======================================		
Create all the backdrop brushes using the tileset loaded in Resouces class
====================================== 
*/
void Listener::CreateBackDropBrushes ()
{
	// Initialize the array of backdrop brushes to the number of surfaces we have
	// loaded in "Resources" class.
	mNumBackDropBrushes = mResources->GetVectorTiles()->size();
	mBackDropBrushes = new BRUSH [mNumBackDropBrushes];

	// Iterate the vector of backdrop images already loaded and create 2d entities
	vector <SURFACE*>::iterator mIter;
	int i = 0;

	for (mIter  = mResources->GetVectorTiles()->begin();
		mIter != mResources->GetVectorTiles()->end();
		mIter++)
	{	
		mBackDropBrushes [i].mId = (*mIter)->mId;								// Id
		mBackDropBrushes [i].mEntity.SetSurface (&(*mIter)->mSurface);			// Set the surface (brush image) into the entity
		mI->Entity2dManager->Add (BRUSH_LAYER, &mBackDropBrushes [i].mEntity);	// Add the entity to the IndieLib manager
		mBackDropBrushes [i].mEntity.SetHotSpot (0.5f, 0.5f);					// Pivot point in the middle of the surface
		mBackDropBrushes [i].mEntity.SetShow (false);							// Hide the brush
		mBackDropBrushes [i].mEntity.SetTransparency (128);						// Brushes are 50% Transparent
		i++;
	}

	// We only show the current brush
	mCurrentBackDropBrush = 0;
	mBackDropBrushes [0].mEntity.SetShow (true);
}


/* 
======================================	
Free the memory used by the brushes
====================================== 
*/
void Listener::DeleteBackDropBrushes ()
{
	// Delete all the brushes
	for (int i = 0; i < mNumBackDropBrushes; i++)
	{
		mI->Entity2dManager->Delete (&mBackDropBrushes[i].mEntity);
	}
	
	// Delete the array of brushes
	delete [] mBackDropBrushes;
}
