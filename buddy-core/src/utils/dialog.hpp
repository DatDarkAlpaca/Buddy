#pragma once
#include <QFileDialog>
#include <core/buddy_settings.hpp>

namespace bud
{
	inline QString openBuddyDialog()
	{
		QStringList mediaExtensionList = BuddySettings::getStrings("project/supported/media_formats");

		QString extensionString;
		size_t index = 0;
		for (const auto& extension : mediaExtensionList)
		{
			extensionString += QString("*.%1").arg(extension);

			if (index - 1 != mediaExtensionList.size())
				extensionString += ' ';

			index++;
		}

		QString supportedSubtitles = QString("Buddy media files (%1)").arg(extensionString);

		return QFileDialog::getOpenFileName(
			nullptr,
			"Open Buddy", "",
			supportedSubtitles
		);
	}
}