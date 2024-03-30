#pragma once
#include <Qt>
#include <QMenu>
#include <QMouseEvent>
#include <utils/dialog.hpp>

#include "ui_mini_buddy.h"

namespace bud
{
	class MiniBuddy : public QMainWindow
	{
		Q_OBJECT;

	public:
		explicit MiniBuddy(QWidget* parent = nullptr)
			: QMainWindow(parent)
		{
			ui.setupUi(this);
			setupWindow();

			setContextMenuPolicy(Qt::CustomContextMenu);
			connect(this, &MiniBuddy::customContextMenuRequested, this, &MiniBuddy::showContextMenu);

			connect(ui.miniBuddyDisplay, &BuddyDisplay::buddySet, [&](const QSize& size) {
				resize(size);
			});

			ui.miniBuddyDisplay->setPixmap(QPixmap("res/sore-crow.png"));
		}

	protected:
		void mousePressEvent(QMouseEvent* event) override
		{
			if (event->button() != Qt::LeftButton)
				return;

			m_Offset = event->globalPosition().toPoint();
			m_Dragging = true;
		}

		void mouseMoveEvent(QMouseEvent* event) override
		{
			if (!m_Dragging)
				return;

			QPoint delta = event->globalPosition().toPoint() - m_Offset;
			move(x() + delta.x(), y() + delta.y());

			clampWidget();

			m_Offset = event->globalPosition().toPoint();
		}

		void mouseReleaseEvent(QMouseEvent* event) override
		{
			if (event->button() != Qt::LeftButton)
				return;

			m_Dragging = false;
		}

	private:
		void setupWindow()
		{
			setWindowFlag(Qt::WindowStaysOnTopHint);
			setWindowFlag(Qt::FramelessWindowHint);
			setAttribute(Qt::WA_TranslucentBackground);

			setStyleSheet("background: transparent");
		}

		void clampWidget()
		{
			QScreen* screen = QGuiApplication::primaryScreen();
			QRect  screenGeometry = screen->geometry();

			int windowX = x();
			windowX = std::clamp(windowX, 0, screenGeometry.width() - width());

			int windowY = y();
			windowY = std::clamp(windowY, 0, screenGeometry.height() - height());
			
			move(windowX, windowY);
		}

	private:
		void showContextMenu(const QPoint& position)
		{
			QPoint item = mapToGlobal(position);
			m_IsContextOpen = true;

			// Creates the menu:
			QMenu contextMenu(tr("Buddy Tools"), this);
			contextMenu.addAction("Open Buddy...");
			contextMenu.addAction("Close");

			QAction* rightClickItem = contextMenu.exec(item);
			if (rightClickItem && rightClickItem->text().contains("Open Buddy..."))
				emit openBuddyPressed();

			if (rightClickItem && rightClickItem->text().contains("Close"))
				emit closePressed();

			connect(&contextMenu, &QMenu::destroyed, [&]() { m_IsContextOpen = false; });
		}

	signals:
		void openBuddyPressed();

		void closePressed();

	public:
		BuddyDisplay* buddyDisplay() const { return ui.miniBuddyDisplay; }

	private:
		Ui::MiniBuddy ui;

	private:
		QPoint m_Offset = QPoint();
		bool m_Dragging = false;
		bool m_IsContextOpen = false;
	};
}