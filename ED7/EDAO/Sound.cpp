#include "edao.h"

PVOID CSound::GetSoundPathByIndex(PSTR SoundPath, ULONG SeIndex)
{
    PVOID Entry;

    Entry = this->GetSeEntryBySoundIndex(SeIndex);
    if (Entry != nullptr)
    {
        return (this->*StubGetSoundPathByIndex)(SoundPath, SeIndex);
    }

    sprintf(SoundPath, "%sed7%c%04d.wav", this->GetSoundDataPath(), SeIndex >= 2000 ? 'v' : 's', SeIndex);
    return nullptr;
}
