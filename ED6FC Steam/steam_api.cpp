#include "ml.h"

#define STEAM_API_NODLL 1
#pragma warning(disable:4819)

#include "steam\steam_api.h"
#include "steam\steam_gameserver.h"

using ml::String;

#if 0
    #define STEAM_LOG(...) (PrintConsole(L"[%S] ", __FUNCTION__), PrintConsole(__VA_ARGS__), PrintConsole(L"\n"))
#else
    #define STEAM_LOG(...)
#endif

#define S_VIRTUAL THISCALL

struct CSteamApps : public ISteamApps
{
public:
    virtual bool S_VIRTUAL BIsSubscribed()
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual bool S_VIRTUAL BIsLowViolence()
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual bool S_VIRTUAL BIsCybercafe()
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual bool S_VIRTUAL BIsVACBanned()
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual PCSTR S_VIRTUAL GetCurrentGameLanguage()
    {
        STEAM_LOG(L"");
        return "japanese";
    }

    virtual PCSTR S_VIRTUAL GetAvailableGameLanguages()
    {
        STEAM_LOG(L"");
        return "japanese";
    }

    virtual bool S_VIRTUAL BIsSubscribedApp(AppId_t appID)
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual bool S_VIRTUAL BIsDlcInstalled(AppId_t appID)
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual uint32 S_VIRTUAL GetEarliestPurchaseUnixTime(AppId_t nAppID)
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual bool S_VIRTUAL BIsSubscribedFromFreeWeekend()
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual int S_VIRTUAL GetDLCCount()
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual bool S_VIRTUAL BGetDLCDataByIndex( int iDLC, AppId_t *pAppID, bool *pbAvailable, char *pchName, int cchNameBufferSize )
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual void S_VIRTUAL InstallDLC( AppId_t nAppID )
    {
        STEAM_LOG(L"");
    }

    virtual void S_VIRTUAL UninstallDLC( AppId_t nAppID )
    {
        STEAM_LOG(L"");
    }

    virtual void S_VIRTUAL RequestAppProofOfPurchaseKey(AppId_t nAppID)
    {
        STEAM_LOG(L"");
    }

    virtual bool S_VIRTUAL GetCurrentBetaName( char *pchName, int cchNameBufferSize )
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual bool S_VIRTUAL MarkContentCorrupt( bool bMissingFilesOnly )
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual uint32 S_VIRTUAL GetInstalledDepots( AppId_t appID, DepotId_t *pvecDepots, uint32 cMaxDepots )
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual uint32 S_VIRTUAL GetAppInstallDir( AppId_t appID, char *pchFolder, uint32 cchFolderBufferSize )
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual bool S_VIRTUAL BIsAppInstalled(AppId_t appID)
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual CSteamID S_VIRTUAL GetAppOwner()
    {
        STEAM_LOG(L"");
        return CSteamID();
    }

    virtual PCSTR S_VIRTUAL GetLaunchQueryParam(PCSTR pchKey)
    {
        STEAM_LOG(L"");
        return "";
    }

    virtual bool GetDlcDownloadProgress(AppId_t nAppID, uint64 *punBytesDownloaded, uint64 *punBytesTotal)
    {
        if (punBytesDownloaded != nullptr)
            *punBytesDownloaded = 1;

        if (punBytesTotal != nullptr)
            *punBytesTotal = 1;

        return true;
    }

    virtual int GetAppBuildId()
    {
        return 0;
    }

#ifdef _PS3
    // Result returned in a RegisterActivationCodeResponse_t callresult
    virtual SteamAPICall_t RegisterActivationCode(const char *pchActivationCode)
    {
        return k_uAPICallInvalid;
    }
#endif
};

struct CSteamClient : public ISteamClient
{
public:
    virtual HSteamPipe S_VIRTUAL CreateSteamPipe()
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual bool S_VIRTUAL BReleaseSteamPipe(HSteamPipe steamPipe)
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual HSteamUser S_VIRTUAL ConnectToGlobalUser(HSteamPipe steamPipe)
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual HSteamUser S_VIRTUAL CreateLocalUser(HSteamPipe *steamPipe, EAccountType accountType)
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual void S_VIRTUAL ReleaseUser(HSteamPipe steamPipe, HSteamUser user)
    {
        STEAM_LOG(L"");
    }

    virtual ISteamUser* S_VIRTUAL GetISteamUser(HSteamUser steamUser, HSteamPipe steamPipe, PCSTR version)
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamGameServer *S_VIRTUAL GetISteamGameServer(HSteamUser steamUser, HSteamPipe steamPipe, PCSTR version)
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual void S_VIRTUAL SetLocalIPBinding(uint32 ip, USHORT port)
    {
        STEAM_LOG(L"");
    }

    virtual ISteamFriends *S_VIRTUAL GetISteamFriends(HSteamUser steamUser, HSteamPipe steamPipe, PCSTR version)
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamUtils *S_VIRTUAL GetISteamUtils(HSteamPipe steamPipe, PCSTR version)
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamMatchmaking *S_VIRTUAL GetISteamMatchmaking(HSteamUser steamUser, HSteamPipe steamPipe, PCSTR version)
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamMatchmakingServers *S_VIRTUAL GetISteamMatchmakingServers(HSteamUser steamUser, HSteamPipe steamPipe, PCSTR version)
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual void *S_VIRTUAL GetISteamGenericInterface(HSteamUser steamUser, HSteamPipe steamPipe, PCSTR version)
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamUserStats* S_VIRTUAL GetISteamUserStats(HSteamUser hSteamUser, HSteamPipe hSteamPipe, const char *pchVersion)
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamGameServerStats *S_VIRTUAL GetISteamGameServerStats(HSteamUser steamUser, HSteamPipe steamPipe, PCSTR version)
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamApps *S_VIRTUAL GetISteamApps(HSteamUser steamUser, HSteamPipe steamPipe, PCSTR version)
    {
        STEAM_LOG(L"");
        return SteamApps();
    }

    virtual ISteamNetworking *S_VIRTUAL GetISteamNetworking(HSteamUser steamUser, HSteamPipe steamPipe, PCSTR version)
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamRemoteStorage *S_VIRTUAL GetISteamRemoteStorage(HSteamUser steamUser, HSteamPipe steamPipe, PCSTR version)
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamScreenshots *GetISteamScreenshots(HSteamUser hSteamuser, HSteamPipe hSteamPipe, const char *pchVersion)
    {
        return nullptr;
    }

    virtual void S_VIRTUAL RunFrame()
    {
        STEAM_LOG(L"");
    }

    virtual uint32 S_VIRTUAL GetIPCCallCount()
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual void S_VIRTUAL SetWarningMessageHook(SteamAPIWarningMessageHook_t function)
    {
        STEAM_LOG(L"");
    }

    virtual bool S_VIRTUAL BShutdownIfAllPipesClosed()
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual class ISteamHTTP * S_VIRTUAL GetISteamHTTP( HSteamUser hSteamuser, HSteamPipe hSteamPipe, PCSTR pchVersion )
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual class ISteamUnifiedMessages * S_VIRTUAL GetISteamUnifiedMessages( HSteamUser hSteamuser, HSteamPipe hSteamPipe, PCSTR pchVersion )
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual class  ISteamController * S_VIRTUAL GetISteamController( HSteamUser hSteamUser, HSteamPipe hSteamPipe, PCSTR pchVersion )
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual class ISteamUGC * S_VIRTUAL GetISteamUGC( HSteamUser hSteamUser, HSteamPipe hSteamPipe, PCSTR pchVersion )
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual class ISteamAppList * S_VIRTUAL GetISteamAppList( HSteamUser hSteamUser, HSteamPipe hSteamPipe, PCSTR pchVersion )
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual class ISteamMusic * S_VIRTUAL GetISteamMusic( HSteamUser hSteamuser, HSteamPipe hSteamPipe, PCSTR pchVersion )
    {
        STEAM_LOG(L"");
        DebugBreakPoint();
        return nullptr;
    }

    virtual ISteamMusicRemote *GetISteamMusicRemote(HSteamUser hSteamuser, HSteamPipe hSteamPipe, const char *pchVersion)
    {
        STEAM_LOG(L"");
        return nullptr;
    }

    virtual ISteamHTMLSurface *GetISteamHTMLSurface(HSteamUser hSteamuser, HSteamPipe hSteamPipe, const char *pchVersion)
    {
        STEAM_LOG(L"");
        return nullptr;
    }

    virtual void Set_SteamAPI_CPostAPIResultInProcess(SteamAPI_PostAPIResultInProcess_t func)
    {
        STEAM_LOG(L"");
    }

    virtual void Remove_SteamAPI_CPostAPIResultInProcess(SteamAPI_PostAPIResultInProcess_t func)
    {
        STEAM_LOG(L"");
    }

    virtual void Set_SteamAPI_CCheckCallbackRegisteredInProcess(SteamAPI_CheckCallbackRegistered_t func)
    {
        STEAM_LOG(L"");
    }

    virtual ISteamInventory *GetISteamInventory(HSteamUser hSteamuser, HSteamPipe hSteamPipe, const char *pchVersion)
    {
        STEAM_LOG(L"");
        return nullptr;
    }

    virtual ISteamVideo *GetISteamVideo(HSteamUser hSteamuser, HSteamPipe hSteamPipe, const char *pchVersion)
    {
        STEAM_LOG(L"");
        return nullptr;
    }
};

struct CSteamUserStats : public ISteamUserStats
{
    SteamLeaderboard_t mLastLeaderboard = 0;

    virtual bool S_VIRTUAL RequestCurrentStats()
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual bool S_VIRTUAL GetStat(PCSTR name, int32 *data )
    {
        STEAM_LOG(L"");
        *data = 0;
        return true;
    };

    virtual bool S_VIRTUAL GetStat(PCSTR name, FLOAT *data)
    {
        STEAM_LOG(L"");
        *data = 0;
        return true;
    }

    virtual bool S_VIRTUAL SetStat(PCSTR name, int32 data)
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual bool S_VIRTUAL SetStat(PCSTR name, FLOAT data)
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual bool S_VIRTUAL UpdateAvgRateStat(PCSTR name, FLOAT countThisSession,  double sessionLength)
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual bool S_VIRTUAL GetAchievement(PCSTR name, bool *achieved)
    {
        STEAM_LOG(L"");
        *achieved = true;
        return true;
    }

    virtual bool S_VIRTUAL SetAchievement(PCSTR name)
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual bool S_VIRTUAL ClearAchievement(PCSTR name)
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual bool S_VIRTUAL GetAchievementAndUnlockTime(PCSTR name,
                              bool *achieved,
                              uint32 *unlockTime)
    {
        STEAM_LOG(L"");
        *achieved = true;
        *unlockTime = 0;
        return true;
    }

    virtual bool S_VIRTUAL StoreStats()
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual int S_VIRTUAL GetAchievementIcon(PCSTR name)
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual PCSTR S_VIRTUAL GetAchievementDisplayAttribute(PCSTR name, PCSTR key)
    {
        STEAM_LOG(L"");
        return "AchievementDisplayAttribute";
    }

    virtual bool S_VIRTUAL IndicateAchievementProgress(PCSTR name, uint32 curProgress, uint32 maxProgress)
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual uint32 S_VIRTUAL GetNumAchievements()
    {
        return 0;
    }

    virtual PCSTR S_VIRTUAL GetAchievementName( uint32 iAchievement )
    {
        return 0;
    }

    virtual SteamAPICall_t S_VIRTUAL RequestUserStats(CSteamID steamIDUser)
    {
        STEAM_LOG(L"");
        return k_uAPICallInvalid;
    }

    virtual bool S_VIRTUAL GetUserStat(CSteamID steamIDUser, PCSTR name, int32 *data)
    {
        STEAM_LOG(L"");
        *data = 0;
        return true;
    }

    virtual bool S_VIRTUAL GetUserStat(CSteamID steamIDUser, PCSTR name, FLOAT *data)
    {
        STEAM_LOG(L"");
        *data = 0;
        return true;
    }

    virtual bool S_VIRTUAL GetUserAchievement(CSteamID steamIDUser, PCSTR name, bool *achieved)
    {
        STEAM_LOG(L"");
        *achieved = true;
        return true;
    }

    virtual bool S_VIRTUAL GetUserAchievementAndUnlockTime(CSteamID steamIDUser, PCSTR name, bool *achieved, uint32 *unlockTime)
    {
        STEAM_LOG(L"");
        *achieved = true;
        *unlockTime = 0;
        return true;
    }

    virtual bool S_VIRTUAL ResetAllStats(bool achievementsToo)
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual SteamAPICall_t S_VIRTUAL FindOrCreateLeaderboard(
            PCSTR leaderboardName,
            ELeaderboardSortMethod leaderboardSortMethod,
            ELeaderboardDisplayType leaderboardDisplayType)
    {
        STEAM_LOG(L"");
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t S_VIRTUAL FindLeaderboard(PCSTR leaderboardName)
    {
        STEAM_LOG(L"");
        return k_uAPICallInvalid;
    }

    virtual PCSTR S_VIRTUAL GetLeaderboardName(SteamLeaderboard_t steamLeaderboard)
    {
        STEAM_LOG(L"");
        return "LeaderboardName";
    }

    virtual int S_VIRTUAL GetLeaderboardEntryCount(SteamLeaderboard_t steamLeaderboard)
    {
        STEAM_LOG(L"");
        mLastLeaderboard = steamLeaderboard;
        return 10;
    }

    virtual ELeaderboardSortMethod S_VIRTUAL GetLeaderboardSortMethod(SteamLeaderboard_t steamLeaderboard)
    {
        STEAM_LOG(L"");
        return k_ELeaderboardSortMethodDescending;
    }

    virtual ELeaderboardDisplayType S_VIRTUAL GetLeaderboardDisplayType(SteamLeaderboard_t steamLeaderboard)
    {
        STEAM_LOG(L"");
        return k_ELeaderboardDisplayTypeNumeric;
    }

    virtual SteamAPICall_t S_VIRTUAL DownloadLeaderboardEntries(SteamLeaderboard_t steamLeaderboard, ELeaderboardDataRequest leaderboardDataRequest, int rangeStart, int rangeEnd)
    {
        STEAM_LOG(L"");
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t S_VIRTUAL DownloadLeaderboardEntriesForUsers(SteamLeaderboard_t hSteamLeaderboard, CSteamID *prgUsers, int cUsers )
    {
        STEAM_LOG(L"");
        return k_uAPICallInvalid;
    }

    virtual bool S_VIRTUAL GetDownloadedLeaderboardEntry(
            SteamLeaderboardEntries_t steamLeaderboardEntries,
            int index,
            LeaderboardEntry_t *leaderboardEntry,
            int32 *details,
            int detailsMax)
    {
        STEAM_LOG(L"");
        *details = 0;
        return false;
    }

    virtual SteamAPICall_t S_VIRTUAL UploadLeaderboardScore(
            SteamLeaderboard_t steamLeaderboard,
            ELeaderboardUploadScoreMethod leaderboardUploadScoreMethod,
            int32 score,
            const int32 *scoreDetails,
            int scoreDetailsCount)
    {
        STEAM_LOG(L"");
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t S_VIRTUAL AttachLeaderboardUGC( SteamLeaderboard_t hSteamLeaderboard, ULONG64 hUGC )
    {
        STEAM_LOG(L"");
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t S_VIRTUAL GetNumberOfCurrentPlayers()
    {
        STEAM_LOG(L"");
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t S_VIRTUAL RequestGlobalAchievementPercentages()
    {
        STEAM_LOG(L"");
        return k_uAPICallInvalid;
    }

    virtual int S_VIRTUAL GetMostAchievedAchievementInfo( char *pchName, uint32 unNameBufLen, FLOAT *pflPercent, bool *pbAchieved )
    {
        STEAM_LOG(L"");
        *pflPercent = 100;
        *pbAchieved = true;
        return 0;
    }

    virtual int S_VIRTUAL GetNextMostAchievedAchievementInfo( int iIteratorPrevious, char *pchName, uint32 unNameBufLen, FLOAT *pflPercent, bool *pbAchieved )
    {
        STEAM_LOG(L"");
        ZeroMemory(pchName, unNameBufLen);
        *pflPercent = 100;
        *pbAchieved = true;
        return 0;
    }

    virtual bool S_VIRTUAL GetAchievementAchievedPercent( PCSTR pchName, FLOAT *pflPercent )
    {
        STEAM_LOG(L"");
        *pflPercent = 100;
        return false;
    }

    virtual SteamAPICall_t S_VIRTUAL RequestGlobalStats( int nHistoryDays )
    {
        STEAM_LOG(L"");
        return k_uAPICallInvalid;
    }

    virtual bool S_VIRTUAL GetGlobalStat( PCSTR pchStatName, int64 *pData )
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual bool S_VIRTUAL GetGlobalStat( PCSTR pchStatName, double *pData )
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual int32 S_VIRTUAL GetGlobalStatHistory( PCSTR pchStatName, int64 *pData, uint32 cubData )
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual int32 S_VIRTUAL GetGlobalStatHistory( PCSTR pchStatName, double *pData, uint32 cubData )
    {
        STEAM_LOG(L"");
        return 0;
    }
};

struct CSteamRemoteStorage : public ISteamRemoteStorage
{
    virtual bool S_VIRTUAL FileWrite(PCSTR FileName, const void* Data, int32 Size)
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual int32 S_VIRTUAL FileRead(PCSTR FileName, PVOID Data, int32 Size)
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual SteamAPICall_t FileWriteAsync(const char *pchFile, const void *pvData, uint32 cubData)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t FileReadAsync(const char *pchFile, uint32 nOffset, uint32 cubToRead)
    {
        return k_uAPICallInvalid;
    }

    virtual bool FileReadAsyncComplete(SteamAPICall_t hReadCall, void *pvBuffer, uint32 cubToRead)
    {
        return k_uAPICallInvalid;
    }

    virtual bool S_VIRTUAL FileForget(PCSTR FileName)
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual bool S_VIRTUAL FileDelete( PCSTR FileName )
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual SteamAPICall_t S_VIRTUAL FileShare( PCSTR FileName )
    {
        STEAM_LOG(L"");
        return k_uAPICallInvalid;
    }

    virtual bool S_VIRTUAL SetSyncPlatforms( PCSTR FileName, ERemoteStoragePlatform eRemoteStoragePlatform )
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual ULONG64 S_VIRTUAL FileWriteStreamOpen( PCSTR FileName )
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual bool S_VIRTUAL FileWriteStreamWriteChunk( ULONG64 writeHandle, const void *pvData, int32 cubData )
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual bool S_VIRTUAL FileWriteStreamClose( ULONG64 writeHandle )
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual bool S_VIRTUAL FileWriteStreamCancel( ULONG64 writeHandle )
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual bool S_VIRTUAL FileExists( PCSTR FileName )
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual bool S_VIRTUAL FilePersisted( PCSTR FileName )
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual int32 S_VIRTUAL GetFileSize( PCSTR FileName )
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual int64 S_VIRTUAL GetFileTimestamp( PCSTR FileName )
    {
        STEAM_LOG(L"");
        return 1;
    }

    virtual ERemoteStoragePlatform S_VIRTUAL GetSyncPlatforms( PCSTR FileName )
    {
        STEAM_LOG(L"");
        return k_ERemoteStoragePlatformWindows;
    }

    virtual int32 S_VIRTUAL GetFileCount()
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual PCSTR S_VIRTUAL GetFileNameAndSize( int iFile, int32 *pnFileSizeInBytes )
    {
        STEAM_LOG(L"");
        *pnFileSizeInBytes = 0;
        return "";
    }

    virtual bool S_VIRTUAL GetQuota(int32 *pnTotalBytes, int32 *puAvailableBytes )
    {
        STEAM_LOG(L"");
        *pnTotalBytes = 0x10000000;
        *puAvailableBytes = 0x10000000;
        return true;
    }

    virtual bool S_VIRTUAL IsCloudEnabledForAccount()
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual bool S_VIRTUAL IsCloudEnabledForApp()
    {
        STEAM_LOG(L"");
        return true;
    }

    virtual void S_VIRTUAL SetCloudEnabledForApp( bool bEnabled )
    {
        STEAM_LOG(L"");
    }

    virtual SteamAPICall_t S_VIRTUAL UGCDownload( ULONG64 hContent, uint32 unPriority )
    {
        STEAM_LOG(L"");
        return k_uAPICallInvalid;
    }

    virtual bool S_VIRTUAL GetUGCDownloadProgress( ULONG64 hContent, int32 *pnBytesDownloaded, int32 *pnBytesExpected )
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual bool S_VIRTUAL GetUGCDetails( ULONG64 hContent, AppId_t *pnAppID, char **ppchName, int32 *pnFileSizeInBytes, CSteamID *pSteamIDOwner )
    {
        STEAM_LOG(L"");
        return false;
    }

    virtual int32 S_VIRTUAL UGCRead(UGCHandle_t hContent, void *pvData, int32 cubDataToRead, uint32 cOffset, EUGCReadAction eAction )
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual int32 S_VIRTUAL GetCachedUGCCount()
    {
        STEAM_LOG(L"");
        return 0;
    }

    virtual ULONG64 S_VIRTUAL GetCachedUGCHandle( int32 iCachedContent )
    {
        STEAM_LOG(L"");
        return 0;
    }

#if defined(_PS3) || defined(_SERVER)
    virtual void GetFileListFromServer()
    {
    }

    virtual bool FileFetch(const char *pchFile)
    {
        return true;
    }

    virtual bool FilePersist(const char *pchFile)
    {
        return true;
    }

    virtual bool SynchronizeToClient()
    {
        return true;
    }

    virtual bool SynchronizeToServer()
    {
        return true;
    }

    virtual bool ResetFileRequestState()
    {
        return true;
    }

#endif

    // publishing UGC
    virtual SteamAPICall_t PublishWorkshopFile(const char *pchFile, const char *pchPreviewFile, AppId_t nConsumerAppId, const char *pchTitle, const char *pchDescription, ERemoteStoragePublishedFileVisibility eVisibility, SteamParamStringArray_t *pTags, EWorkshopFileType eWorkshopFileType)
    {
        return k_uAPICallInvalid;
    }

    virtual PublishedFileUpdateHandle_t CreatePublishedFileUpdateRequest(PublishedFileId_t unPublishedFileId)
    {
        return k_PublishedFileUpdateHandleInvalid;
    }

    virtual bool UpdatePublishedFileFile(PublishedFileUpdateHandle_t updateHandle, const char *pchFile)
    {
        return true;
    }

    virtual bool UpdatePublishedFilePreviewFile(PublishedFileUpdateHandle_t updateHandle, const char *pchPreviewFile)
    {
        return true;
    }

    virtual bool UpdatePublishedFileTitle(PublishedFileUpdateHandle_t updateHandle, const char *pchTitle)
    {
        return true;
    }

    virtual bool UpdatePublishedFileDescription(PublishedFileUpdateHandle_t updateHandle, const char *pchDescription)
    {
        return true;
    }

    virtual bool UpdatePublishedFileVisibility(PublishedFileUpdateHandle_t updateHandle, ERemoteStoragePublishedFileVisibility eVisibility)
    {
        return true;
    }

    virtual bool UpdatePublishedFileTags(PublishedFileUpdateHandle_t updateHandle, SteamParamStringArray_t *pTags)
    {
        return true;
    }

    virtual SteamAPICall_t CommitPublishedFileUpdate(PublishedFileUpdateHandle_t updateHandle)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t GetPublishedFileDetails(PublishedFileId_t unPublishedFileId, uint32 unMaxSecondsOld)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t DeletePublishedFile(PublishedFileId_t unPublishedFileId)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t EnumerateUserPublishedFiles(uint32 unStartIndex)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t SubscribePublishedFile(PublishedFileId_t unPublishedFileId)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t EnumerateUserSubscribedFiles(uint32 unStartIndex)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t UnsubscribePublishedFile(PublishedFileId_t unPublishedFileId)
    {
        return k_uAPICallInvalid;
    }

    virtual bool UpdatePublishedFileSetChangeDescription(PublishedFileUpdateHandle_t updateHandle, const char *pchChangeDescription)
    {
        return true;
    }

    virtual SteamAPICall_t GetPublishedItemVoteDetails(PublishedFileId_t unPublishedFileId)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t UpdateUserPublishedItemVote(PublishedFileId_t unPublishedFileId, bool bVoteUp)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t GetUserPublishedItemVoteDetails(PublishedFileId_t unPublishedFileId)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t EnumerateUserSharedWorkshopFiles(CSteamID steamId, uint32 unStartIndex, SteamParamStringArray_t *pRequiredTags, SteamParamStringArray_t *pExcludedTags)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t PublishVideo(EWorkshopVideoProvider eVideoProvider, const char *pchVideoAccount, const char *pchVideoIdentifier, const char *pchPreviewFile, AppId_t nConsumerAppId, const char *pchTitle, const char *pchDescription, ERemoteStoragePublishedFileVisibility eVisibility, SteamParamStringArray_t *pTags)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t SetUserPublishedFileAction(PublishedFileId_t unPublishedFileId, EWorkshopFileAction eAction)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t EnumeratePublishedFilesByUserAction(EWorkshopFileAction eAction, uint32 unStartIndex)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t EnumeratePublishedWorkshopFiles(EWorkshopEnumerationType eEnumerationType, uint32 unStartIndex, uint32 unCount, uint32 unDays, SteamParamStringArray_t *pTags, SteamParamStringArray_t *pUserTags)
    {
        return k_uAPICallInvalid;
    }

    virtual SteamAPICall_t UGCDownloadToLocation(UGCHandle_t hContent, const char *pchLocation, uint32 unPriority)
    {
        return k_uAPICallInvalid;
    }

};

//////////////////////////////////////////////////////////////////////////
// export
//////////////////////////////////////////////////////////////////////////

static CSteamApps apps;
static CSteamUserStats stat;
static CSteamClient client;
static CSteamRemoteStorage storage;

bool S_CALLTYPE SteamAPI_Init()
{
    STEAM_LOG(L"");
    return true;
}

bool S_CALLTYPE SteamAPI_InitSafe()
{
    STEAM_LOG(L"");
    return false;
}

bool S_CALLTYPE SteamAPI_IsSteamRunning()
{
    STEAM_LOG(L"");
    return true;
}

void S_CALLTYPE SteamAPI_RegisterCallResult(struct CallbackBase *callback, SteamAPICall_t apiCall)
{
    STEAM_LOG(L"");
}

void S_CALLTYPE SteamAPI_RegisterCallback(struct CallbackBase *callback, int iCallback)
{
    STEAM_LOG(L"");
}

bool S_CALLTYPE SteamAPI_RestartAppIfNecessary(uint32 appId)
{
    STEAM_LOG(L"");
    return false;
}

void S_CALLTYPE SteamAPI_RunCallbacks()
{
    STEAM_LOG(L"");
}

void S_CALLTYPE SteamAPI_SetMiniDumpComment(PCSTR msg)
{
    STEAM_LOG(L"");
}

void S_CALLTYPE SteamAPI_Shutdown()
{
    STEAM_LOG(L"");
}

void S_CALLTYPE SteamAPI_UnregisterCallResult(struct CallbackBase *callback, SteamAPICall_t apiCall)
{
    STEAM_LOG(L"");
}

void S_CALLTYPE SteamAPI_UnregisterCallback(struct CallbackBase *callback)
{
    STEAM_LOG(L"");
}

void S_CALLTYPE SteamAPI_WriteMiniDump(uint32 exceptionCode, PVOID exceptionInfo, uint32 buildId)
{
    STEAM_LOG(L"");
}

ISteamApps* S_CALLTYPE SteamApps()
{
    STEAM_LOG(L"");
    return &apps;
}

ISteamUserStats* S_CALLTYPE SteamUserStats()
{
    STEAM_LOG(L"");
    return &stat;
}

ISteamClient* S_CALLTYPE SteamClient()
{
    STEAM_LOG(L"");
    return &client;
}

ISteamFriends* S_CALLTYPE SteamFriends()
{
    STEAM_LOG(L"");
    DebugBreakPoint();
    return nullptr;
}

ISteamGameServer* S_CALLTYPE SteamGameServer()
{
    STEAM_LOG(L"");
    DebugBreakPoint();
    return nullptr;
}

ISteamNetworking* S_CALLTYPE SteamGameServerNetworking()
{
    STEAM_LOG(L"");
    DebugBreakPoint();
    return nullptr;
}

ULONG64 S_CALLTYPE SteamGameServer_GetSteamID()
{
    STEAM_LOG(L"");
    return 251150;
}

bool S_CALLTYPE SteamGameServer_Init(uint32 ip, USHORT port, USHORT gamePort, USHORT spectatorPort, USHORT queryPort, EServerMode serverMode, PCSTR gameDir, PCSTR versionString)
{
    STEAM_LOG(L"");
    return true;
}

void S_CALLTYPE SteamGameServer_RunCallbacks()
{
    STEAM_LOG(L"");
}

void S_CALLTYPE SteamGameServer_Shutdown()
{
    STEAM_LOG(L"");
}

ISteamMatchmaking* S_CALLTYPE SteamMatchmaking()
{
    STEAM_LOG(L"");
    DebugBreakPoint();
    return nullptr;
}

ISteamMatchmakingServers* S_CALLTYPE SteamMatchmakingServers()
{
    STEAM_LOG(L"");
    DebugBreakPoint();
    return nullptr;
}

ISteamNetworking* S_CALLTYPE SteamNetworking()
{
    STEAM_LOG(L"");
    DebugBreakPoint();
    return nullptr;
}

ISteamRemoteStorage* S_CALLTYPE SteamRemoteStorage()
{
    STEAM_LOG(L"");
    return &storage;
}

ISteamScreenshots* S_CALLTYPE SteamScreenshots()
{
    STEAM_LOG(L"");
    return nullptr;
}
