/*****************************************************************************************
/* Desc: Map class, for loading and savin maps and creating, cloning and deleting nodes.
/*
/* gametuto.com - Javier L�pez L�pez (javilop.com)
/*
/*****************************************************************************************
/*
/* Creative Commons - Attribution 3.0 Unported
/* You are free:
/*	to Share � to copy, distribute and transmit the work
/*	to Remix � to adapt the work
/*
/* Under the following conditions:
/* Attribution. You must attribute the work in the manner specified by the author or licensor 
/* (but not in any way that suggests that they endorse you or your use of the work).
/*
/*****************************************************************************************/

// ------ Includes -----

#include "Map.h"


/* 
======================================									
Init
====================================== 
*/
Map::Map() 
{
	// Get IndieLib instante
	mI = CIndieLib::Instance();
}


/* 
======================================									
Free memory
====================================== 
*/
void Map::Free() 
{
	// Free all the map nodes
	FreeMap ();
}


/* 
======================================									
Create node
====================================== 
*/
void Map::CreateNode (int pX, int pY, int pZ, int pId, int pLayer, IND_Surface *pSurface)
{
	Node *mNode = new Node (pX, pY, pZ, pId, pLayer, pSurface);
	mNode->GetEntity()->SetPosition ((float) pX, (float) pY, 0);
	mVectorNodes.push_back (mNode);
}


/* 
======================================									
Clone node
====================================== 
*/
void Map::CloneNode (Node *pNode)
{
	// Create a new node
	Node *mNewNode = new Node	((int) pNode->GetEntity()->GetPosX(), 
								(int) pNode->GetEntity()->GetPosY(), 
								(int) pNode->GetEntity()->GetPosZ() - 1, 
								pNode->GetSurfaceId(),
								pNode->GetLayer(), 
								pNode->GetEntity()->GetSurface());

	// Copy attributes from the source entity (original node) to the new cloned entity (new node)
	mNewNode->GetEntity()->SetAngleXYZ (0, 0, pNode->GetEntity()->GetAngleZ());
	mNewNode->GetEntity()->SetScale (pNode->GetEntity()->GetScaleX(), pNode->GetEntity()->GetScaleX());
	mNewNode->GetEntity()->SetTransparency (pNode->GetEntity()->GetTransparency());
	mNewNode->GetEntity()->SetMirrorX (pNode->GetEntity()->GetMirrorX());
	mNewNode->GetEntity()->SetMirrorY (pNode->GetEntity()->GetMirrorY());
	mNewNode->GetEntity()->SetTint (pNode->GetEntity()->GetTintR(), pNode->GetEntity()->GetTintG(), pNode->GetEntity()->GetTintB());
	mNewNode->GetEntity()->ToggleWrap (pNode->GetEntity()->IfWrap());
	mNewNode->GetEntity()->SetRegion (0, 0, pNode->GetEntity()->GetRegionWidth(), pNode->GetEntity()->GetRegionHeight());

	// Add the node to the vector
	mVectorNodes.push_back (mNewNode);
}


/* 
======================================									
Delete node
====================================== 
*/
void Map::DeleteNode (Node *pNode)
{
	vector <Node*>::iterator mIter;

	Node *mTemp;

	for (mIter  = mVectorNodes.begin();
		mIter != mVectorNodes.end();
		mIter++)
	{	
		if ((*mIter) == pNode)
		{	
			mTemp = *mIter;
			mIter = mVectorNodes.erase (mIter);
			delete mTemp;
			break;
		}	
	}
}


/* 
======================================									
Save the map (the vector of nodes containing each entity) to an XML file
====================================== 
*/
bool Map::SaveMap (char *pTilesetPath)
{
	char *mPath = OpenFileDialog ("XML\0*.xml;", false, "Choose a location to save the map file");

	if (!strcmp (mPath, "")) 
	{
		delete [] mPath;
		return false;
	}

	TiXmlDocument mXmlDoc;

	// XML Declaration
 	TiXmlDeclaration *mDecl = new TiXmlDeclaration ("1.0", "", "");  
	mXmlDoc.LinkEndChild (mDecl);  
 
	// Map tag
	TiXmlElement *mXRoot = new TiXmlElement ("map");  
	mXmlDoc.LinkEndChild (mXRoot);  

	// Tileset
	TiXmlElement *mXTileset = new TiXmlElement ("tileset");  
	mXRoot->LinkEndChild (mXTileset);  

	char mCurrentDir[MAX_PATH];
	GetCurrentDirectory (MAX_PATH, mCurrentDir);									// Get current directory path
	mXTileset->SetAttribute("tileset_file", pTilesetPath + strlen (mCurrentDir));	// Only gets the relative path to the tileset

	// Iterate the nodes vector and write them to the XML
	TiXmlElement *mXNodes = new TiXmlElement ("nodes");   
	mXRoot->LinkEndChild (mXNodes); 

	vector <Node*>::iterator mIter;

	for (mIter  = mVectorNodes.begin();
		mIter != mVectorNodes.end();
		mIter++)
	{	
		TiXmlElement *mXNode;
		mXNode = new TiXmlElement ("node");  
		mXNode->SetAttribute ("surface_id", (*mIter)->GetSurfaceId());
		mXNode->SetAttribute ("x", (int) (*mIter)->GetEntity()->GetPosX());
		mXNode->SetAttribute ("y", (int) (*mIter)->GetEntity()->GetPosY());
		mXNode->SetAttribute ("z", (*mIter)->GetEntity()->GetPosZ());
		mXNode->SetAttribute ("layer", (*mIter)->GetLayer());
		mXNode->SetDoubleAttribute ("angle", (*mIter)->GetEntity()->GetAngleZ());
		mXNode->SetDoubleAttribute ("scale", (*mIter)->GetEntity()->GetScaleX());
		mXNode->SetAttribute ("trans", (*mIter)->GetEntity()->GetTransparency());
		mXNode->SetAttribute ("mirror_x", (*mIter)->GetEntity()->GetMirrorX());
		mXNode->SetAttribute ("mirror_y", (*mIter)->GetEntity()->GetMirrorY());
		mXNode->SetAttribute ("tint_r", (*mIter)->GetEntity()->GetTintR());
		mXNode->SetAttribute ("tint_g", (*mIter)->GetEntity()->GetTintG());
		mXNode->SetAttribute ("tint_b", (*mIter)->GetEntity()->GetTintB());
		mXNode->SetAttribute ("if_wrap", (*mIter)->GetEntity()->IfWrap());
		mXNode->SetAttribute ("region_width", (*mIter)->GetEntity()->GetRegionWidth());
		mXNode->SetAttribute ("region_height", (*mIter)->GetEntity()->GetRegionHeight());
		mXNodes->LinkEndChild (mXNode); 		
	}

	// Save the map to an XML file
	mXmlDoc.SaveFile (mPath);  

	// Free memory (XML nodes are deleted by TiXmlDocument destructor)
	delete mPath;

	return true;
}


/* 
======================================									
Load a Map from a XML file and create a node vector
====================================== 
*/
bool Map::LoadMap (Resources *pResources)
{
	char *mPath = OpenFileDialog ("XML\0*.xml;", true, "Choose a map file");

	if (!strcmp (mPath, "")) 
	{
		delete [] mPath;
		return true;
	}

	// Free current map
	FreeMap();

	// Initializa XML doc
	TiXmlDocument mXmlDoc (mPath);

	// Fatal error, cannot load
	if (!mXmlDoc.LoadFile())
	{
		return false;
	}

	// Document root
	TiXmlElement *mXMap = 0;
	mXMap = mXmlDoc.FirstChildElement("map");

	if (!mXMap)
	{
		// No "<map>" tag
		return false;
	}

	// ----------------- Parse tileset -----------------

	// Tileset
	TiXmlElement *mXTileset = 0;
	mXTileset = mXMap->FirstChildElement("tileset");

	if (!mXTileset)
	{
		// No "<tileset>" tag
		return false;
	}

	// Id
	if (mXTileset->Attribute("tileset_file"))
	{
		char mPath [MAX_PATH];
		GetCurrentDirectory (MAX_PATH, mPath);								// Get the path to the current directory
		strcat (mPath, (char *) mXTileset->Attribute("tileset_file"));		// Add the name of the tileset to the path
		if (!pResources->LoadTileset (mPath)) return 0;						// It tries to load the tiles
	}

	// ----------------- Parse nodes -----------------

	// Nodes
	TiXmlElement *mXNodes = 0;
	mXNodes = mXMap->FirstChildElement("nodes");

	if (!mXNodes)
	{
		// No "<nodes>" tag
		return false;
	}

	TiXmlElement *mXNode = 0;
	mXNode = mXNodes->FirstChildElement("node");

	if (!mXNode)
	{
		// No nodes to parse
		return false;
	}
	
	// Parse all the nodes

	while (mXNode)
	{
		// Parameters to parse
		int mSurfaceId, mX, mY, mZ, mLayer, mTrans, mTintR, mTintG, mTintB, mRegionWidth, mRegionHeight;
		bool mMirrorX, mMirrorY, mIfWrap;
		float mAngle, mScale;
	

		// Surface Id
		if (mXNode->Attribute("surface_id"))
		{
			mSurfaceId = atoi (mXNode->Attribute("surface_id"));
		}
		else
		{
			return false;
		}

		// Pos X
		if (mXNode->Attribute("x"))
		{
			mX = atoi (mXNode->Attribute("x"));
		}
		else
		{
			return false;
		}

		// Pos Y
		if (mXNode->Attribute("y"))
		{
			mY = atoi (mXNode->Attribute("y"));
		}
		else
		{
			return false;
		}

		// Pos Z
		if (mXNode->Attribute("z"))
		{
			mZ = atoi (mXNode->Attribute("z"));
		}
		else
		{
			return false;
		}

		// Layer
		if (mXNode->Attribute("layer"))
		{
			mLayer = atoi (mXNode->Attribute("layer"));
		}
		else
		{
			return false;
		}

		// Angle
		if (mXNode->Attribute("angle"))
		{
			mAngle = (float) atof (mXNode->Attribute("angle"));
		}
		else
		{
			return false;
		}

		// Scale
		if (mXNode->Attribute("scale"))
		{
			mScale = (float) atof (mXNode->Attribute("scale"));
		}
		else
		{
			return false;
		}

		// Transparency
		if (mXNode->Attribute("trans"))
		{
			mTrans = atoi (mXNode->Attribute("trans"));
		}
		else
		{
			return false;
		}

		// Mirror x
		if (mXNode->Attribute("mirror_x"))
		{
			mMirrorX = (bool) atoi (mXNode->Attribute("mirror_x"));
		}
		else
		{
			return false;
		}

		// Mirror y
		if (mXNode->Attribute("mirror_y"))
		{
			mMirrorY = atoi (mXNode->Attribute("mirror_y"));
		}
		else
		{
			return false;
		}

		// Tint r
		if (mXNode->Attribute("tint_r"))
		{
			mTintR = atoi (mXNode->Attribute("tint_r"));
		}
		else
		{
			return false;
		}

		// Tint g
		if (mXNode->Attribute("tint_g"))
		{
			mTintG = atoi (mXNode->Attribute("tint_g"));
		}
		else
		{
			return false;
		}

		// Tint b
		if (mXNode->Attribute("tint_b"))
		{
			mTintB = atoi (mXNode->Attribute("tint_b"));
		}
		else
		{
			return false;
		}

		// If wrap
		if (mXNode->Attribute("if_wrap"))
		{
			mIfWrap = atoi (mXNode->Attribute("if_wrap"));
		}
		else
		{
			return false;
		}

		// Region width
		if (mXNode->Attribute("region_width"))
		{
			mRegionWidth = atoi (mXNode->Attribute("region_width"));
		}
		else
		{
			return false;
		}

		// Region height
		if (mXNode->Attribute("region_height"))
		{
			mRegionHeight = atoi (mXNode->Attribute("region_height"));
		}
		else
		{
			return false;
		}

		// Get the surface of the tile already loaded in Resources class by passing the Id
		IND_Surface *mSurface = pResources->GetSurfaceById(mSurfaceId);
		if (mSurface == (IND_Surface *) -1) return 0;

		// Node creation, we have to set the surface later
		Node *mNewNode = new Node (mX, mY, mZ, mSurfaceId, mLayer, mSurface);

		// Set new node attributes
		mNewNode->GetEntity()->SetAngleXYZ (0, 0, mAngle);
		mNewNode->GetEntity()->SetScale (mScale, mScale);
		mNewNode->GetEntity()->SetTransparency (mTrans);
		mNewNode->GetEntity()->SetMirrorX (mMirrorX);
		mNewNode->GetEntity()->SetMirrorY (mMirrorY);
		mNewNode->GetEntity()->SetTint (mTintR, mTintG, mTintB);
		mNewNode->GetEntity()->ToggleWrap (mIfWrap);
		mNewNode->GetEntity()->SetRegion (0, 0, mRegionWidth, mRegionHeight);

		// Push the node into the nodes vector
		mVectorNodes.push_back (mNewNode);
	
		// Move to the next declaration
		mXNode = mXNode->NextSiblingElement("node");
	}

	// Free memory, XML nodes are deleted by TiXmlDocument destructor
	delete mPath;

	return true;
}


/* 
======================================									
Gets the path to the tileset file that we are going to load
====================================== 
*/
char *Map::GetPathToTileset ()
{
	char *mPath = OpenFileDialog ("XML\0*.xml;", true, "Choose a Tileset file");

	if (!strcmp (mPath, "")) 
	{
		delete [] mPath;
		return 0;
	}

	return mPath;
}


/* 
======================================									
Delete all the map nodes
====================================== 
*/
void Map::FreeMap ()
{
	vector <Node*>::iterator mIter;

	for (mIter  = mVectorNodes.begin();
		mIter != mVectorNodes.end();
		++mIter)
	{
		mI->Entity2dManager->Delete ((*mIter)->GetEntity());
		delete (*mIter);
	}

	mVectorNodes.clear();
}


// --------------------------------------------------------------------------------
//									Private methods
// --------------------------------------------------------------------------------

/*
==================
Open a Windows open / save dialog
pAction = if true => open dialog if false => save dialog
==================
*/
char *Map::OpenFileDialog (char *pFilter, bool pAction, char *pTitle)
{	
	// If we are in full screen mode, we have to change to screen mode
	bool mKeepFullScreen = false;
	if (mI->Window->IsFullScreen())
	{
		mI->Render->ToggleFullScreen ();
		mKeepFullScreen = true;
	}

	OPENFILENAME mOpenFileName;
	char szFile[MAX_PATH];
	char mCurrentDir[MAX_PATH];

	szFile[0] = 0;
	GetCurrentDirectory (MAX_PATH, mCurrentDir);

	mOpenFileName.lStructSize = sizeof (OPENFILENAME);
	mOpenFileName.hwndOwner = mI->Window->GetWnd();
	mOpenFileName.lpstrFilter = pFilter;
	mOpenFileName.lpstrCustomFilter = NULL;
	mOpenFileName.nMaxCustFilter = 0;
	mOpenFileName.nFilterIndex = 0;
	mOpenFileName.lpstrFile = szFile;
	mOpenFileName.nMaxFile = sizeof( szFile );
	mOpenFileName.lpstrFileTitle = 0;
	mOpenFileName.nMaxFileTitle = 0;
	mOpenFileName.lpstrInitialDir = mCurrentDir;
	mOpenFileName.lpstrTitle = pTitle;
	mOpenFileName.nFileOffset = 0;
	mOpenFileName.nFileExtension = 0;
	mOpenFileName.lpstrDefExt = NULL;
	mOpenFileName.lCustData = 0;
	mOpenFileName.lpfnHook = NULL;
	mOpenFileName.lpTemplateName = NULL;
	mOpenFileName.Flags = OFN_FILEMUSTEXIST | OFN_NOCHANGEDIR; // Keep the relative part intact.

	char *mResult = new char [MAX_PATH];

	if (pAction)
	{
		if (GetOpenFileName (&mOpenFileName))
		{
			if (mKeepFullScreen)	mI->Render->ToggleFullScreen ();
			strcpy (mResult, szFile);
			return mResult;
		}
		else
			return "";
	}
	else
	{
		if (GetSaveFileName (&mOpenFileName))
		{
			if (mKeepFullScreen)	mI->Render->ToggleFullScreen ();
			strcpy (mResult, szFile);
			return mResult;
		}
		else
			return "";
	}
}


